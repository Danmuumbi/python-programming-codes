def is_leap(year):
    """defines leap years"""#this is a docstring
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_month(year, month):
    """defines months of the year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

days = days_month(year, month)
print(days)
