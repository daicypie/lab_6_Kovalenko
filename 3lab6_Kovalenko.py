def is_year_leap(year):
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


def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None

    # Список кількості днів у місяцях (січень - грудень)
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Якщо рік високосний, лютому додаємо 1 день
    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]


def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Підрахунок кількості днів до вказаного дня
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)

    # Додавання днів поточного місяця
    day_of_year += day

    return day_of_year


# Тестування функції
test_cases = [
    (1937, 12, 21, 355),
    (2000, 12, 31, 366),
    (2004, 1, 28, 28),
    (2005, 5, 27, 147),
    (2010, 5, 5, 125),
    (2010, 10, 10, 283),
    (2024, 10, 17, 291)
]

for year, month, day, expected in test_cases:
    result = day_of_year(year, month, day)
    if result == expected:
        print(f"day_of_year({year}, {month}, {day}) = {result} -> OK")
    else:
        print(f"day_of_year({year}, {month}, {day}) = {result} -> Failed, expected {expected}")
