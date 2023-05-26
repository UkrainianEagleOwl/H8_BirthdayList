from datetime import datetime, timedelta
from collections import defaultdict
import const_test_users



def get_next_monday_date():
    current_datetime = datetime.now()
    days_to_monday = (0 - current_datetime.weekday()) % 7
    next_monday = current_datetime + timedelta(days=days_to_monday)
    next_monday_datetime = next_monday.replace(
        hour=0, minute=0, second=0, microsecond=0)
    return(next_monday_datetime)

def get_this_year_date_bithday(birthday_date):
    current_datetime = datetime.now()
    this_year_birthday = datetime(year = current_datetime.year,month = birthday_date.month,day=birthday_date.day)
    return this_year_birthday

def get_str_name_day(day_number):
    match day_number:
        case 0:
            return 'Monday'
        case 1:
            return 'Tuesday'
        case 2:
            return 'Wednesday'
        case 3:
            return 'Thursday'
        case 4:
            return 'Friday'


    

def get_birthdays_per_week(users):
    check_date = get_next_monday_date()
    check_week = [check_date + timedelta(days = i) for i in range(-2,5)]
    birthday_week = defaultdict(list)
    for person in users:
        d = person.get('birthday')
        d = get_this_year_date_bithday(d)
        if d in check_week:
            weekday = d.weekday()
            if weekday == (6 or 7):
                weekday = 0
            birthday_week[weekday].append(person.get('name'))
    for day, name in birthday_week.items():
        print(f'{get_str_name_day(day)} : {", ".join(name)}')
                                  
if __name__ == '__main__':
    get_birthdays_per_week(const_test_users.CONST_USERS_TEST)
