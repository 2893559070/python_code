import random

# if
num = random.random()
flag = False

if flag != False:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

# 下方的代码没有缩进到if语句块，所以和if条件无关
print('我是无论条件是否成立都要执行的代码')
print(f'{num}')


# if else
age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
else:
    print(f'您的年龄是{age},未成年，请自行回家写作业')

print('系统关闭')

# if elif else
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您的年龄是{age},童工一枚')
elif (age >= 18) and (age <= 60):
    print(f'您的年龄是{age},合法工龄')
elif age > 60:
    print(f'您的年龄是{age},可以退休')