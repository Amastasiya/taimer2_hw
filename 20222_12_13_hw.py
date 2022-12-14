# Считается, что Вы знаете, что такое високосный год
# (делится на 4 и не делится на 100 или делится на 400)
# Считается, что Вы знаете, сколько дней в каждом месяце
# Считается известным, что в неделе 7 дней
#
#
# 1. Сегодня вторник, 13-е декабря 2022 года
# Используя только эту информацию вычислить день недели нового года.
# Подсказка: правильный ответ: воскресенье
#
# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.
#
# 3. В какой день недели Вы родились? Перечислить все свои ДР,
# пришедшиеся на тот же день недели.
import time
from datetime import datetime
from datetime import date

today = datetime.now()
print("Сегодня", today)

#today = datetime(2022, 12, 13)
def data():
    day, month, year = map(int, input("Введите дату в формате ДД ММ ГГГГ: ").split())
    return year, month, day
user_y, user_m, user_d = data()

#def user():
    #year = int(input("Введите год: "))
    #month = int(input("Введите месяц: "))
    #day = int(input("Введите день: "))
    #return year, month, day
#user_y, user_m, user_d = user()

# проверка года високосный или нет
def year(user_y):
    if (user_y % 4 == 0 and user_y % 100 != 0) or user_y % 400 == 0:
        return True
    else:
        return False
print(year(user_y))

# проверка месяца
def month(user_m):
    if user_m <= 12 and user_m > 0:
        return True
    return False
print(month(user_m))

# проверка дней в месяце
def in_month_of_days(m, y):
    if m == 2:
        if year(y):
            return 29
        return 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31
print("В этом месяце", in_month_of_days(user_m, user_y))

# определили по дате какой это был день недели
def week(y, m, d):
    day = datetime(y, m, d).weekday()
    wd = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(wd[day])
week(user_y, user_m, user_d)

# определение дня недели без datetime
def week_day(y, m, d):
    if (m == 1 or m == 2):
        y -=1
    m -= 2
    if m <= 0:
        m += 12
    c = y // 100
    y = y - c * 100
    wk = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
    number_week = {0: "Воскресенье",
                   1: "Понедельник",
                   2: "Вторник",
                   3: "Среда",
                   4: "Четверг",
                   5: "Пятница",
                   6: "Суббота"}
    result = number_week.get(wk)
    return result
print(week_day(user_y, user_m, user_d))

def search_happy_new_year(today):
    user = int(input("Напишите любой год: "))
    today_year = today.year
    for y in range(user, today_year):
        if date(y, 1, 1).weekday() == 0: #or date(y, 1, 1).weekday() == 1:
            print(y, "- в понедельник")
        if date(y, 1, 1).weekday() == 1:
            print(y, "- во вторник")

print(search_happy_new_year(today))

def happy_birthday(today):
    user = int(input("Напишите год рождения: "))
    today_year = today.year
    print("В эти года день рождение был в понедельник")
    for y in range(user, today_year):
        if date(y, 10, 29).weekday() == 0:
            print(y)

(happy_birthday(today))





