import 'package:flutter/material.dart';
import 'settings_controller.dart';

class SettingsView extends StatelessWidget {
  const SettingsView({super.key, required this.controller});

  static const routeName = '/settings';

  final SettingsController controller;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: ListView(
        children: [
          SwitchListTile(
            title: const Text('Dark Mode'),
            value: controller.themeMode == ThemeMode.dark,
            onChanged: (bool isDarkMode) {
              controller.updateThemeMode(
                isDarkMode ? ThemeMode.dark : ThemeMode.light,
              );
            },
          )
        ],
      ),
    );
  }
}
