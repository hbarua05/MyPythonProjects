import re


def isDateValid(day, month, year):
    """Check if a date is valid given day, month and year.

    Args:
        day (integer): an int representing a day
        month (integer): an int representing a month
        year (integer): an int representing a year

    Returns:
        Boolean: True if date exists and False if date does not exist
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 30

    elif month in [4, 6, 9, 11]:
        return day <= 31
    elif month == 2:
        if year % 400 == 0:
            return day <= 29
        elif year % 4 == 0 and not year % 100 == 0:
            return day <= 29
        else:
            return day <= 28
    return False


dateRegex = re.compile(r"""(
    ([0][1-9] | [1-2]\d | [3][0-1])/      # day in DD
    ([0][1-9] | [1][0-2])/       # month in MM
    ([1-2]\d{3})        # year in YYYY(1000-2999)
)""", re.VERBOSE)

date = dateRegex.search("today's date is 04/02/2021")
if date:
    day, month, year = int(date.group(2)), int(
        date.group(3)), int(date.group(4))
    print(isDateValid(day, month, year))
