# 定义装饰器
import time


def decorator(fun):
    def inner():
        # 内部函数对已有函数进行封装
        begin = time.time()
        print(f'begin {begin}')

        fun()

        end = time.time()
        print(f'end {end}')

    return inner

@decorator
def work():
    for i in range(1000000):
        # print(i)
        i

work()
