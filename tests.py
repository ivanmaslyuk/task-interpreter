from main import interpret, makeResponse
from date_helper import next_weekday, Weekday
import datetime

def assert_string(s, o, name):
    result = interpret(s)
    success = result == o
    if (success):
        print("Test " + name + " succeeded.")
    else:
        print("Test " + name + " failed.")
        print(result)

def test1():
    s = "Сделать дз по диффурам до пятницы"
    o = makeResponse("Сделать дз по диффурам", "", datetime.date(2019, 4, 4), True, "none")
    assert_string(s, o, "1")


def test2():
    s = "Доделать шахматы до пятницы"
    o = makeResponse("Доделать шахматы", "", datetime.date(2019, 4, 4), True, "none")
    assert_string(s, o, "2")

def test3():
    s = "Написать курсовую до 12 апреля"
    o = makeResponse("Написать курсовую", "", datetime.date(2019, 4, 11), True, "none")
    assert_string(s, o, "3")

def test4():
    s = "Сходить за документами завтра"
    o = makeResponse("Сходить за документами", "", datetime.date(2019, 3, 30), False, "none")
    assert_string(s, o, "4")

def test5():
    s = "Забрать отчет"
    o = makeResponse("Забрать отчет", "", datetime.date(2019, 3, 29), False, "none")
    assert_string(s, o, "5")

def test6():
    s = "Закомментировать код и отправить его научному руководителю послезавтра"
    o = makeResponse("Закомментировать код и отправить его научному руководителю", "", datetime.date(2019, 3, 31), False, "none")
    assert_string(s, o, "6")

def test7():
    s = "Сходить за инн в следующую пятницу"
    o = makeResponse("Сходить за инн", "", next_weekday(Weekday.FRIDAY), False, "none")
    assert_string(s, o, "7")

def test8():
    s = "Сходить за инн до следующей пятницы"
    o = makeResponse("Сходить за инн", "", next_weekday(Weekday.THURSDAY), True, "none")
    assert_string(s, o, "8")

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()