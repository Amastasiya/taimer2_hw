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

today = datetime(2022, 12, 13)

def user():
    year = int(input("Введите год рождения: "))
    month = int(input("Введите месяц рождения: "))
    day = int(input("Введите день рождения: "))
    return year, month, day
user_y, user_m, user_d = user()

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
print(in_month_of_days(user_m, user_y))

#def week(y, m, d):
    #day = y, m, d
    #week_day = date.weekday(day)
    #wd = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    #print(wd[week_day])
#week(user_y, user_m, user_d)

