# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100
# объектов. Выведите количество различных объектов в этом списке.

objects = [1, 2, 3, 3, True, False, True]  # comment it on stepic
result = set()
for object in objects:
    result.add(str(object))
print(len(result))
