import 'package:flutter/material.dart';
import 'package:graphql_flutter/graphql_flutter.dart';

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
      }
    }
  """;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // AppBar with Custom Color
        title: Image.asset(
          Theme.of(context).brightness == Brightness.dark
              ? 'assets/images/app_logo_inverted.png' // Replace with your dark theme logo's path
              : 'assets/images/app_logo.png', // Replace with your light theme logo's path
          height: 40, // Adjust the height of the logo
        ),
        centerTitle: true, // Ensure the logo is centered
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: () {
              Navigator.restorablePushNamed(context, SettingsView.routeName);
            },
          ),
        ],
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Add your title inside the body
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Center(
              child: Text(
                'Choose Parking', // Replace with your desired title
                style: Theme.of(context).textTheme.headlineLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
              ),
            ),
          ),
          Expanded(
            child: Query(
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

                return ListView.builder(
                  restorationId: 'mapItemListView',
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
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
