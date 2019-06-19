import datetime
from date_helper import Weekday, next_weekday, is_string_weekday, tomorrow, today, Month, is_string_month, day_after_tomorrow

def interpret(s: str):
    words = s.split(" ")

    # данные
    date = today()
    hasDeadline = False
    name = ""
    description = ""
    color = "none"

    for i in range(len(words)):
        word = words[i]
        if word == "до":
            word2 = ""
            wordInBetween = False
            try:
                word2 = words[i+1]
                if word2.startswith("следующ"):
                    word2 = words[i+2]
                    wordInBetween = True
            except:
                print("не удалось считать word2")

            if is_string_weekday(word2):
                date = calculate_next_weekday(word2)
                date -= datetime.timedelta(days=1)
                hasDeadline = True
                # удалить дату из строки
                del words[i]
                del words[i]
                if wordInBetween:
                    del words[i]

                break

            if word2 == "завтра":
                date = today()
                hasDeadline = False
                # удалить дату из строки
                del words[i]
                del words[i]
                if wordInBetween:
                    del words[i]

                break

            # если word2 - это число (до 25 января)
            if word2.isnumeric() and int(word2) in range(1, 31+1):
                word3 = ""
                try:
                    word3 = words[i+2]
                except:
                    print("не удалось считать word3")
                if is_string_month(word3):
                    month = month_from_string(word3)
                    date = date_from_month_and_day(int(word2), month)
                    date -= datetime.timedelta(days=1)
                    hasDeadline = True
                    del words[i]
                    del words[i]
                    del words[i]
                    break

        if word == "в" or word == "во":
            word2 = ""
            wordInBetween = False
            try:
                word2 = words[i+1]
                if word2.startswith("следующ"):
                    word2 = words[i+2]
                    wordInBetween = True
            except:
                print("не удалось считать word2")
            
            if is_string_weekday(word2):
                wd = calculate_next_weekday(word2)
                date = wd
                del words[i]
                del words[i]
                if wordInBetween:
                    del words[i]
                break
                

        if word == "завтра":
            date = tomorrow()
            del words[i]
            break

        if word == "сегодня":
            date = today()
            del words[i]
            break

        if word == "послезавтра":
            date = day_after_tomorrow()
            del words[i]
            break

    #записываем имя
    for w in words:
        name += w + " "
    name = name.strip()

    # чтобы обнулить секунды и тд и тп
    date = datetime.date(date.year, date.month, date.day)

    return makeResponse(name, description, date, hasDeadline, color)
            

def makeResponse(name: str, description: str, date: datetime.date, hasDeadline: bool, color: str):
    o = dict()
    o["name"] = name
    o["description"] = description
    o["date"] = date
    o["has_deadline"] = hasDeadline
    o["color"] = color
    return o


def calculate_next_weekday(word: str):
    date = datetime.date
    if word.startswith("понедельник"):
        date = next_weekday(Weekday.MONDAY)
    if word.startswith("вторник"):
        date = next_weekday(Weekday.TUESDAY)
    if word.startswith("сред"):
        date = next_weekday(Weekday.WEDNESDAY)
    if word.startswith("четверг"):
        date = next_weekday(Weekday.THURSDAY)
    if word.startswith("пятниц"):
        date = next_weekday(Weekday.FRIDAY)
    if word.startswith("суббот"):
        date = next_weekday(Weekday.SATURDAY)
    if word.startswith("воскресень"):
        date = next_weekday(Weekday.SUNDAY)
    return date

def month_from_string(word: str):
    month = Month.JANUARY
    if word.startswith("январ"):
        month = Month.JANUARY
    if word.startswith("феврал"):
        month = Month.FEBRUARY
    if word.startswith("март"):
        month = Month.MARCH
    if word.startswith("апрел"):
        month = Month.APRIL
    if word == "май" or word == "мая":
        month = Month.MAY
    if word.startswith("июн"):
        month = Month.JUNE
    if word.startswith("июл"):
        month = Month.JULY
    if word.startswith("август"):
        month = Month.AUGUST
    if word.startswith("сентябр"):
        month = Month.SEPTEMBER
    if word.startswith("октябр"):
        month = Month.OCTOBER
    if word.startswith("ноябр"):
        month = Month.NOVEMBER
    if word.startswith("декабр"):
        month = Month.DECEMBER
    return month

def date_from_month_and_day(day: int, month: Month):
    return datetime.date(today().year, month.value, day)