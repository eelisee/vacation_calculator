from PySide6.QtWidgets import QApplication
from settings_window import SettingsDialog
from calendar_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    # Voreinstellungen anzeigen
    settings_dialog = SettingsDialog()
    if settings_dialog.exec():
        settings = settings_dialog.settings  # Vom Dialog zurückgegebene Einstellungen

        # Hauptkalenderfenster anzeigen
        main_window = MainWindow(settings)
        main_window.show()
        app.exec()
        