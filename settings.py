class Settings:
    def __init__(self, year=2025, min_employees=None, region="West", holidays=None, bridge_days=None, close_periods=None):
        self.year = year
        self.min_employees = min_employees or [1, 1, 1, 1, 1, 1, 1]
        self.region = region
        self.holidays = holidays or []
        self.bridge_days = bridge_days or []
        self.close_periods = close_periods or []