# 捕获单个异常
try:
    # 可能发生错误的代码
    global num
    num = 1 / 0
except ZeroDivisionError:
    # 捕获错误
    print('ZeroDivisionError')

# 捕获多个指定异常
try:
    # 可能发生错误的代码
    num = 1 / 0
    print(num1)
except (SyntaxError, NameError, ZeroDivisionError) as Error:
    # 捕获错误
    print(Error, 'Error')

# 捕获所有异常
try:
    # 可能发生错误的代码
    print(num1)
except Exception as Error:
    # 捕获错误
    print(Error, 'Exception')


# 异常else
try:
    # 可能发生错误的代码
    print('num1')
except Exception as Error:
    # 捕获错误
    print(Error, 'Exception')
else:
    print('没有异常的时候执行的代码')

# 异常finally
try:
    # 可能发生错误的代码
    print('num1')
    # 自定义异常抛出
    raise SyntaxError
except Exception as Error:
    # 捕获错误
    print(Error, 'Exception')
finally:
    print('正常与异常的时候都会执行的代码')





