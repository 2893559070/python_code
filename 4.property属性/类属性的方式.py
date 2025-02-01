class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def getAge(self):
        # 获取私有属性
        return self.__age

    def setAge(self, num):
        self.__age = num

    age = property(getAge, setAge)

student = Student()
student.age = 20
age = student.age
print(age)
