import 'package:flutter/material.dart';
import 'package:graphql_flutter/graphql_flutter.dart';
import 'src/app.dart';
import 'src/settings/settings_controller.dart';
import 'src/settings/settings_service.dart';
import 'src/graphql/graphql_config.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';

Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // Handle background messages
  print("Handling a background message: ${message.messageId}");
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize Firebase
  await Firebase.initializeApp();

  // Initialize Hive for offline storage (GraphQL)
  await initHiveForFlutter();

  // Set up the SettingsController
  final settingsController = SettingsController(SettingsService());
  await settingsController.loadSettings();

  // Configure background message handling
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

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
