import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'package:latlong2/latlong.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

import '../settings/settings_view.dart';
import 'map_item_details_view.dart';

void _getDeviceToken(BuildContext context) async {
  String? token = await FirebaseMessaging.instance.getToken();
  print("Device Token: $token");

  if (token != null) {
    _registerDeviceToken(context, token);
  }
}

void _registerDeviceToken(BuildContext context, String token) async {
  const String mutation = """
    mutation RegisterDevice(\$token: String!) {
      registerDevice(pushToken: \$token) {
        success
      }
    }
  """;

  final GraphQLClient client = GraphQLProvider.of(context).value;

  try {
    final QueryResult result = await client.mutate(
      MutationOptions(
        document: gql(mutation),
        variables: {'token': token},
      ),
    );

    if (result.hasException) {
      print("Error saving device token: ${result.exception}");
    } else {
      final bool success = result.data?['registerDevice']['success'] ?? false;
      if (success) {
        print("Device token registered successfully!");
      } else {
        print("Failed to register device token.");
      }
    }
  } catch (e) {
    print("Error during token registration: $e");
  }
}

class SampleItemListView extends StatefulWidget {
  const SampleItemListView({super.key});

  static const routeName = '/';

  @override
  State<SampleItemListView> createState() => _SampleItemListViewState();
}

class _SampleItemListViewState extends State<SampleItemListView> {
  final String query = """
    query GetParkings {
      allParkings {
        identifier
        name
        address
        totalLots
        occupiedLots
        latitude
        longitude
      }
    }
  """;

  @override
  void initState() {
    super.initState();
    _requestNotificationPermissions();
    _configureFirebaseMessaging();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _getDeviceToken(context);
    });
  }

  /// Request notification permissions
  Future<void> _requestNotificationPermissions() async {
    FirebaseMessaging messaging = FirebaseMessaging.instance;

    NotificationSettings settings = await messaging.requestPermission(
      alert: true,
      badge: true,
      sound: true,
    );

    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      print('User granted permission');
    } else if (settings.authorizationStatus ==
        AuthorizationStatus.provisional) {
      print('User granted provisional permission');
    } else {
      print('User declined or has not accepted permission');
    }
  }

  /// Configure Firebase Messaging
  void _configureFirebaseMessaging() {
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      if (message.notification != null) {
        print(
            'Foreground notification received: ${message.notification?.title}');
        print('Message body: ${message.notification?.body}');
      }
    });

    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      print('Notification clicked: ${message.notification?.title}');
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Image.asset(
          Theme.of(context).brightness == Brightness.dark
              ? 'assets/images/app_logo_inverted.png'
              : 'assets/images/app_logo.png',
          height: 40,
        ),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: () {
              Navigator.restorablePushNamed(context, SettingsView.routeName);
            },
          ),
        ],
      ),
      body: Query(
        options: QueryOptions(
          document: gql(query),
          pollInterval: const Duration(seconds: 30),
        ),
        builder: (QueryResult result,
            {VoidCallback? refetch, FetchMore? fetchMore}) {
          if (result.isLoading) {
            return const Center(child: CircularProgressIndicator());
          }

          if (result.hasException) {
            return Center(
              child: Text('Error: ${result.exception.toString()}'),
            );
          }

          final List parkings = result.data?['allParkings'] ?? [];

          final List<Marker> markers = parkings.asMap().entries.map((entry) {
            int index = entry.key;
            var parking = entry.value;
            return Marker(
              point: LatLng(
                double.parse(parking['latitude']),
                double.parse(parking['longitude']),
              ),
              child: GestureDetector(
                onTap: () {
                  Navigator.restorablePushNamed(
                    context,
                    SampleItemDetailsView.routeName,
                    arguments: parking,
                  );
                },
                child: Stack(
                  alignment: Alignment.center,
                  children: [
                    const Icon(
                      Icons.location_on_sharp,
                      color: Colors.red,
                    ),
                    Text(
                      '${index + 1}',
                      style: const TextStyle(
                        color: Colors.black,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            );
          }).toList();

          return Column(
            children: [
              Expanded(
                flex: 2,
                child: FlutterMap(
                  options: MapOptions(
                    initialCenter: markers.isNotEmpty
                        ? markers.first.point
                        : const LatLng(0, 0), // Default to (0,0) if no markers
                    minZoom: 11,
                  ),
                  children: [
                    TileLayer(
                      urlTemplate:
                          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                      subdomains: const ['a', 'b', 'c'],
                      userAgentPackageName: 'com.look4park.parking',
                    ),
                    MarkerLayer(markers: markers),
                  ],
                ),
              ),
              Expanded(
                flex: 1,
                child: ListView.builder(
                  itemCount: parkings.length,
                  itemBuilder: (BuildContext context, int index) {
                    final parking = parkings[index];

                    return ListTile(
                      title: Text('${index + 1}. ${parking['name']}'),
                      subtitle: Text(parking['address']),
                      leading: const CircleAvatar(
                        child: Icon(Icons.location_on),
                      ),
                      onTap: () {
                        Navigator.restorablePushNamed(
                          context,
                          SampleItemDetailsView.routeName,
                          arguments: parking,
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
