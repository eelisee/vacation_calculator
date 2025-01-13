import sqlite3

class VacationDatabase:
    def __init__(self, db_name="vacation_allocator.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            min_days INTEGER,
            rest_days INTEGER,
            work_days TEXT,
            child_care TEXT,
            vacation_preferences TEXT
        )""")
        self.conn.commit()

    def add_employee(self, employee: Employee):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO employees (name, min_days, rest_days, work_days, child_care, vacation_preferences)
        VALUES (?, ?, ?, ?, ?, ?)""",
                       (employee.name, employee.min_days, employee.rest_days, ",".join(map(str, employee.work_days)),
                        ",".join(map(str, employee.child_care)), ",".join(map(str, employee.vacation_preferences))))
        self.conn.commit()

    def get_employees(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        return [Employee(row[1], row[2], row[3], row[4].split(","), row[5].split(","), row[6].split(",")) for row in rows]