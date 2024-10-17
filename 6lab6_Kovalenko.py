def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

    # Тестувальні функції
print(is_a_triangle(1, 2, 3))
print(is_a_triangle(2, 3, 4))
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(4, 5, 6))
print(is_a_triangle(5, 6, 7))
print(is_a_triangle(6, 7, 8))
print(is_a_triangle(7, 8, 9))