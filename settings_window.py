from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QComboBox, QPushButton, QCalendarWidget
from settings import Settings
import datetime

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voreinstellungen")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        # Jahr auswählen
        year_layout = QHBoxLayout()
        year_layout.addWidget(QLabel("Jahr:"))
        self.year_spinbox = QSpinBox()
        self.year_spinbox.setRange(1900, 2100)
        self.year_spinbox.setValue(datetime.date.today().year)
        year_layout.addWidget(self.year_spinbox)
        layout.addLayout(year_layout)

        # Mindestmitarbeiter pro Tag
        min_employees_layout = QVBoxLayout()
        min_employees_layout.addWidget(QLabel("Mindestmitarbeiter pro Tag:"))
        self.min_employees_spinboxes = []
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        for day in days:
            day_layout = QHBoxLayout()
            day_label = QLabel(day)
            spinbox = QSpinBox()
            spinbox.setRange(0, 100)
            spinbox.setValue(1)
            day_layout.addWidget(day_label)
            day_layout.addWidget(spinbox)
            min_employees_layout.addLayout(day_layout)
            self.min_employees_spinboxes.append(spinbox)
        layout.addLayout(min_employees_layout)

        # Region auswählen
        region_layout = QHBoxLayout()
        region_layout.addWidget(QLabel("Region:"))
        self.region_combobox = QComboBox()
        self.region_combobox.addItems(["West", "Ost"])
        region_layout.addWidget(self.region_combobox)
        layout.addLayout(region_layout)

        # Betriebsferien
        self.close_period_calendar = QCalendarWidget()
        self.close_period_calendar.setGridVisible(True)
        layout.addWidget(QLabel("Betriebsferien:"))
        layout.addWidget(self.close_period_calendar)

        # Bestätigungsbutton
        confirm_button = QPushButton("Bestätigen")
        confirm_button.clicked.connect(self.confirm_settings)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def confirm_settings(self):
        self.settings = Settings(
            year=self.year_spinbox.value(),
            min_employees=[spinbox.value() for spinbox in self.min_employees_spinboxes],
            region=self.region_combobox.currentText(),
            holidays=[],  # Feiertage können später geladen werden
            close_periods=[self.close_period_calendar.selectedDate()]
        )
        self.accept()