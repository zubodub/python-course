# objects = [1, 2, 3, 3, True, False, True]
result = set()
for object in objects:
    result.add(str(object))
print(len(result))