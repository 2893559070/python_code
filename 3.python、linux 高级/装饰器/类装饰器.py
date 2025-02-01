class MyDecorator(object):

 def __init__(self, func):
     self.func = func

# 实现call 这个方法，让对象变成可调用的对象，可调用的对象能够像函数使用
 def __call__(self, *args, **kwargs):
     # 对已有函数进行封装
     print("课已经讲完了")
     return self.func(*args, **kwargs)

# @MyDecorator => show = MyDecorator(show)
@MyDecorator
def show():
    print("下课了")

show()

