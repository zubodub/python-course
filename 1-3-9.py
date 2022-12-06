# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую
# самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5

# вариант 1
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        while x % 5 != 0:
            x += 1
    return x

# вариант 2
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        multiplier = (x + 5 - 1) // 5
        x = 5 * multiplier
    return x