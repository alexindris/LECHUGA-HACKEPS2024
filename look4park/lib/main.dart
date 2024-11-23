import 'package:flutter/material.dart';
import 'package:graphql_flutter/graphql_flutter.dart';

import 'src/app.dart';
import 'src/settings/settings_controller.dart';
import 'src/settings/settings_service.dart';
import 'src/graphql/graphql_config.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await initHiveForFlutter();

  final settingsController = SettingsController(SettingsService());

  await settingsController.loadSettings();

  // Initialize GraphQL Client
  final ValueNotifier<GraphQLClient> graphqlClient =
      GraphQLConfig.initializeClient();

  runApp(
    GraphQLProvider(
      client: graphqlClient,
      child: CacheProvider(
        child: MyApp(settingsController: settingsController),
      ),
    ),
  );
}
