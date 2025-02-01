list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(x):
    return x % 2

result = filter(func, list1)

print(result)
print(list(result))
