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

# Тестові дані
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

# Перевірка результатів
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")