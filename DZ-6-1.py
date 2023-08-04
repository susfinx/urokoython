
import sys
from datetime import datetime

def check_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return True, date.strftime('%A')
    except ValueError:
        return False, None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python date_checker.py YYYY-MM-DD")
    else:
        input_date = sys.argv[1]
        is_valid, day_of_week = check_date(input_date)
        
        if is_valid:
            print(f"The date {input_date} is valid and falls on a {day_of_week}.")
        else:
            print(f"The date {input_date} is not valid.")
