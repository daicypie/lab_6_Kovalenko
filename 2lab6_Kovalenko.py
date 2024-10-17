def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            # Перевірка чи високосний рік, якщо воно ділиться на 400
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

    # Якщо рік високосний, лютому додамо 1 день
    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]


# Тестування функції
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
