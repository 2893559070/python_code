# 第一种写法 import math
# print(f'{math.sqrt(9)} : sqrt')

# 第二种写法
# from math import sqrt
# print(f'{sqrt(9)} : sqrt')

# 第三种写法
from math import *
print(f'{sqrt(9)} : sqrt')

# 第四种写法
from my_module import *
print(f'{my_function()} : sqrt')


# 引入包
from mypages.index import *
from mypages.my_module import init as index2_init

res = init()
res2 = index2_init()

print(res)
print(res2)
