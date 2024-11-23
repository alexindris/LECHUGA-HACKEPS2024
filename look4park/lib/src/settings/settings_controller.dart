import 'package:flutter/material.dart';
import 'settings_service.dart';

class SettingsController with ChangeNotifier {
  SettingsController(this._settingsService);

  final SettingsService _settingsService;

  late ThemeMode _themeMode;

  ThemeMode get themeMode => _themeMode;

  /// Load settings at the start of the app.
  Future<void> loadSettings() async {
    _themeMode = await _settingsService.themeMode();
    notifyListeners();
  }

  /// Update and persist theme settings.
  Future<void> updateThemeMode(ThemeMode theme) async {
    _themeMode = theme;
    notifyListeners();
    await _settingsService.updateThemeMode(theme);
  }
}
