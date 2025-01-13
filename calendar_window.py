from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QWidget
import datetime

class MainWindow(QMainWindow):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.setWindowTitle(f"Urlaubskalender {self.settings.year}")
        self.setMinimumWidth(800)

        layout = QVBoxLayout()

        # Kalenderübersicht
        self.calendar_table = QTableWidget(0, 7)  # 7 Spalten für die Wochentage
        self.calendar_table.setHorizontalHeaderLabels(["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"])
        self.populate_calendar()
        layout.addWidget(self.calendar_table)

        # Mitarbeiter hinzufügen Button
        add_employee_button = QPushButton("Mitarbeiter hinzufügen")
        add_employee_button.clicked.connect(self.add_employee)
        layout.addWidget(add_employee_button)

        # Set Main Layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_calendar(self):
        """Populates the calendar with the selected year's dates and events."""
        year = self.settings.year
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

        current_date = start_date
        row = 0
        while current_date <= end_date:
            if current_date.weekday() == 0:  # Neue Woche
                self.calendar_table.insertRow(row)
            col = current_date.weekday()
            item = QTableWidgetItem(current_date.strftime("%d.%m.%Y"))
            self.calendar_table.setItem(row, col, item)
            current_date += datetime.timedelta(days=1)
            if current_date.weekday() == 0:
                row += 1

    def add_employee(self):
        """Dialog to add a new employee."""
        print("Neuen Mitarbeiter hinzufügen")