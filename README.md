# vacation_calculator
Calculator for the allocation of leave days

## Basic Functionality

This project aims to create a resource allocation tool for managers to optimally allocate employee vacation days, ensuring that every employee feels respected and valued. The tool, ideally a desktop application or at least a user-friendly tool, will simplify the calculation process for non-programmers.

### Key Features

1. **Employee Count and Minimum Presence**:
    - The tool considers the total number of employees, denoted as `x`.
    - A percentage `alpha_i` of employees must be present on day `i` of the week, calculated as `alpha_i * x = y_i`.

2. **Yearly Calendar**:
    - The year is displayed in a calendar or table format with weekdays, dates, and calendar weeks.
    - The year can be selected flexibly, accounting for leap years.

3. **Company Closure Periods**:
    - Automatic vacation days for all employees during company closure periods (e.g., Christmas to January 1st, bridge days, and holidays).
    - Option to select between East and West for holidays.

4. **Employee and Manager Management**:
    - Add and rename employees and managers via a button.
    - Each employee and manager has a minimum number of vacation days, which can be individually set and supplemented with special leave.
    - Remaining vacation from the previous year must be used by March and is prioritized for use.

5. **Workdays and Vacation Preferences**:
    - Employees specify their working days and preferred vacation days, marked as:
      - `+` for "must-have" vacation days.
      - `?` for "optional" vacation days.

6. **Manager Vacation Impact**:
    - When a manager takes a vacation, the minimum required employee presence can be reduced by one.

7. **Priority for Employees with Children**:
    - Employees with children are prioritized for vacation during school holidays and other important periods like kindergarten closures.

### Optimization Problem

The vacation allocation problem is an optimization problem that can be approached from both top-down and bottom-up perspectives. The goal is to ensure regular employee attendance and fair distribution of vacation days throughout the year.

This tool will allow employers to input all relevant parameters and constraints, facilitating the optimal allocation of vacation days for their employees.