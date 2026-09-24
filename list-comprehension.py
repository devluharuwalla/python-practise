

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1,11)]

print(doubles)