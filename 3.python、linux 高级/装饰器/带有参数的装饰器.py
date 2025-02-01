def return_decorator(flag):
    def decorator(func):
        def inner(a, b):

            if(flag == '+'):
                print("正在努力执行加法计算")
            elif(flag == '-'):
                print("正在努力执行减法计算")

            func(a, b)

        return inner
    return decorator

@return_decorator("+")
def add_num(a, b):
    result = a + b
    print(result)

@return_decorator("-")
def sub_num(a, b):
    result = a - b
    print(result)

add_num(1, 3)
sub_num(3, 1)
