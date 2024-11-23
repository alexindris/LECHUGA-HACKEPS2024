import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'package:latlong2/latlong.dart';

import '../settings/settings_view.dart';
import 'map_item_details_view.dart';

class SampleItemListView extends StatelessWidget {
  const SampleItemListView({super.key});

  static const routeName = '/';

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

          // Create markers for each parking location
          final List<Marker> markers = parkings.map((parking) {
            return Marker(
              point: LatLng(
                double.parse(parking['latitude']),
                double.parse(parking['longitude']),
              ),
              child: const Icon(
                Icons.location_on,
                color: Colors.red,
                size: 30,
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
                    minZoom: 12,
                  ),
                  children: [
                    TileLayer(
                      urlTemplate:
                          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                      subdomains: const ['a', 'b', 'c'],
                      userAgentPackageName: 'com.example.app',
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
                      title: Text(parking['name']),
                      subtitle: Text(parking['address']),
                      leading: const CircleAvatar(
                        foregroundImage:
                            AssetImage('assets/images/flutter_logo.png'),
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
