import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:graphql_flutter/graphql_flutter.dart';

import 'map/map_item_details_view.dart';
import 'map/map_item_list_view.dart';
import 'settings/settings_controller.dart';
import 'settings/settings_view.dart';
import 'graphql/graphql_config.dart'; // Add this for your GraphQL configuration

/// The Widget that configures your application.
class MyApp extends StatelessWidget {
  const MyApp({
    super.key,
    required this.settingsController,
  });

  final SettingsController settingsController;

  @override
  Widget build(BuildContext context) {
    // Initialize GraphQL client
    final ValueNotifier<GraphQLClient> graphqlClient =
        GraphQLConfig.initializeClient();

    return GraphQLProvider(
      client: graphqlClient,
      child: CacheProvider(
        child: ListenableBuilder(
          listenable: settingsController,
          builder: (BuildContext context, Widget? child) {
            return MaterialApp(
              restorationScopeId: 'app',

              // Localization delegates for internationalization
              localizationsDelegates: const [
                AppLocalizations.delegate,
                GlobalMaterialLocalizations.delegate,
                GlobalWidgetsLocalizations.delegate,
                GlobalCupertinoLocalizations.delegate,
              ],
              supportedLocales: const [
                Locale('en', ''), // English, no country code
              ],

              // Application title based on localization
              onGenerateTitle: (BuildContext context) =>
                  AppLocalizations.of(context)!.appTitle,

              // Dynamic Themes
              theme: _lightTheme(),
              darkTheme: _darkTheme(),
              themeMode: settingsController.themeMode,

              // Named route handling
              onGenerateRoute: (RouteSettings routeSettings) {
                return MaterialPageRoute<void>(
                  settings: routeSettings,
                  builder: (BuildContext context) {
                    switch (routeSettings.name) {
                      case SettingsView.routeName:
                        return SettingsView(controller: settingsController);
                      case SampleItemDetailsView.routeName:
                        return const SampleItemDetailsView();
                      case SampleItemListView.routeName:
                      default:
                        return const SampleItemListView();
                    }
                  },
                );
              },
            );
          },
        ),
      ),
    );
  }

  /// Light theme configuration
  ThemeData _lightTheme() {
    return ThemeData(
      primaryColor: const Color(0xFFE0F2FE), // Light blue
      appBarTheme: const AppBarTheme(
        backgroundColor: Color(0xFFE0F2FE),
        iconTheme: IconThemeData(color: Colors.black),
        titleTextStyle: TextStyle(color: Colors.black, fontSize: 20),
      ),
      scaffoldBackgroundColor: Colors.white,
      textTheme: const TextTheme(
          titleLarge: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
          bodyMedium: TextStyle(fontSize: 16.0),
          bodySmall: TextStyle(fontSize: 14.0),
          headlineLarge: TextStyle(
              color: const Color(0xFF0369A1), fontWeight: FontWeight.bold)),
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: Color(0xFF0288D1),
        foregroundColor: Colors.white,
      ),
    );
  }

  /// Dark theme configuration
  ThemeData _darkTheme() {
    return ThemeData.dark().copyWith(
      primaryColor: const Color(0xFF121212), // Dark primary color
      appBarTheme: const AppBarTheme(
        backgroundColor: Color(0xFF1F1F1F),
        iconTheme: IconThemeData(color: Colors.white),
        titleTextStyle: TextStyle(color: Colors.white, fontSize: 20),
      ),
      scaffoldBackgroundColor: const Color(0xFF121212),
      textTheme: const TextTheme(
        titleLarge: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
        bodyMedium: TextStyle(fontSize: 16.0, color: Colors.white),
        bodySmall: TextStyle(fontSize: 14.0, color: Colors.white70),
      ),
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: Color(0xFF0288D1),
        foregroundColor: Colors.white,
      ),
    );
  }
}
