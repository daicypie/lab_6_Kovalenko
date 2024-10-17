def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    # Перевірка за допомогою теореми Піфагора
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

    # Тестувальні функції
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(16, 2, 14))
print(is_a_right_triangle(6, 1, 3))
print(is_a_right_triangle(1, 7, 9))
print(is_a_right_triangle(7, 24, 25))
print(is_a_right_triangle(5, 12, 13))