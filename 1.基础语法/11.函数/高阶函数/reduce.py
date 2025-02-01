import functools

def func(a, b) :
    return a + b

res = functools.reduce(func, [1, 2, 3, 4])

print(res)


