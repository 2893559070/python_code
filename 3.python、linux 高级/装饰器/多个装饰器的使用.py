# 通用的装饰器 可以装饰任意类型的函数

def decorator1(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args, **kwargs):

        # args：      元组类型
        # kwargs：    字典类型

        # 添加功能扩展
        print("正在执行功能")

        # 在内部函数里面对已有函数进行装饰
        # *args:把元组里面的每一个元素，按照位置参数的方式进行传参
        # **kwargs:把字典里面的每一个键值对，按照关键字的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        result = func(*args, **kwargs)
        return f'<p>{ result }</p>'
    return inner

def decorator2(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args, **kwargs):

        # args：      元组类型
        # kwargs：    字典类型

        # 添加功能扩展
        print("正在执行功能")

        # 在内部函数里面对已有函数进行装饰
        # *args:把元组里面的每一个元素，按照位置参数的方式进行传参
        # **kwargs:把字典里面的每一个键值对，按照关键字的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        result = func(*args, **kwargs)
        return f'<div>{ result }</div>'
    return inner

# 装饰带有参数的函数
# 多个装饰器的过程:由内到外的一个装饰过程，先执行内部的装饰器，在执行外部的装饰器
@decorator1
@decorator2
def add_num(*args, **kwargs):
    result = "多个装饰器"
    return result

print(add_num())



