# 学习装饰器目的:对已有函数进行额外的功能扩展, 装饰器本质上一个闭包函数,也就是说他也是一个函数嵌套
# 装饰器的特点:
# 1.不修改已有函数的源代码
# 2.不修改已有函数的调用方式
# 3.给以后函数添加额外的功能

# 装饰器
# 如果闭包函数的参数有且只有一个并且是函数类型，那么这个闭包函数称为装饰器
def decorator(func):
    def inner():

        # 添加功能扩展
        print("已添加登录验证")

        # 在内部函数里面对已有函数进行装饰
        func()
    return inner

# 装饰器的写法 “comment = decorator(comment)” 语法糖
@decorator
def comment():
    print("发表评论")

# 调用装饰器对已有函数进行装饰comment=inner
# comment = decorator(comment)

comment()
