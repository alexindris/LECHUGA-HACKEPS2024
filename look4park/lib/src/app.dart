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

              // Themes and theme mode
              theme: ThemeData(),
              darkTheme: ThemeData.dark(),
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
}
