import datetime
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

def today():
    day = datetime.datetime.now()
    return datetime.date(day.year, day.month, day.day)

def next_weekday(wd: Weekday):
    day = today()
    i = 0
    while (True):
        i = i + 1
        day += datetime.timedelta(days=1)
        if day.isoweekday() == wd.value:
            return day

def is_string_weekday(s: str):
    weekdays = ["понедельник", "вторник", "сред", "четверг", "пятниц", "суббот", "воскресень"]
    for weekday in weekdays:
        if s.startswith(weekday):
            return True
    return False

def is_string_month(s: str):
    months = ["январ", "феврал", "январ", "март", "апрел", "июн", "июл", "август", "сентябр", "ноябр", "декабр"]
    for month in months:
        if s.startswith(month):
            return True
    if s == "май" or s == "мая":
        return True
    return False

def tomorrow():
    return today() + datetime.timedelta(days=1)

def day_after_tomorrow():
    return tomorrow() + datetime.timedelta(days=1)