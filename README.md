
# Birthdays Reminder Script

## Overview
This Python script helps in reminding the birthdays of colleagues in the upcoming week. It takes a list of users with their names and birth dates and generates a dictionary indicating whose birthdays fall on each day of the next week.

## Features
- **User Data Handling**: Works with a list of dictionaries, each containing a user's name and birthday.
- **Weekly Birthday Reminders**: Outputs a dictionary mapping days of the week to the names of users having birthdays.
- **Weekend Birthdays Handling**: Moves weekend birthdays to Monday for the upcoming week greetings.
- **Annual Update**: Accounts for birthdays that have already passed in the current year.
- **Empty List Handling**: Functions correctly with an empty list of users.
- **Flexible Date Handling**: Utilizes `datetime.date` for date operations and works with `date.today()` for current date determination.
- **PEP 8 Compliance**: Code written following PEP 8 standards for Python coding.

## Usage
1. Prepare a list of users in the format:
   ```python
   users = [
       {"name": "User1", "birthday": datetime.date(YYYY, MM, DD)},
       {"name": "User2", "birthday": datetime.date(YYYY, MM, DD)},
       ...
   ]
   ```
2. Run the script to get the weekly birthday reminders:
   ```python
   birthdays_this_week = get_birthdays_per_week(users)
   ```

## Function `get_birthdays_per_week`
- **Input**: List of user dictionaries with `name` and `birthday`.
- **Output**: Dictionary mapping weekdays to user names who have birthdays in the next week.
- Example Output:
  ```python
  {'Monday': ['Alice', 'Bob'], 'Wednesday': ['Charlie']}
  ```

## Installation
Clone the repository and ensure Python is installed on your system. The script requires no external dependencies.
