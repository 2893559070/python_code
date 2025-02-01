class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    # 当对象调用age属性的时候会执行下面的方法
    @property
    def age(self):
        # 获取私有属性
        return self.__age

    # 当对象调用age属性设置值的时候会调用下面的方法
    @age.setter
    def age(self, num):
        self.__age = num

student = Student()
student.age = 20
age = student.age
print(age)
