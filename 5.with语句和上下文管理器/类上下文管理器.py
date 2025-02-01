# 一个类只要实现了__enter__()和__exit__()这个两个方法，通过该类创建的对象我们就称之为上下文管理器。
# 上下文管理器可以使用 with 语句，with语句之所以这么强大，背后是由上下文管理器做支撑的，也就是说刚才使用 open 函数创建的文件对象就是就是一个上下文管理器对象。

class File(object):

    # 初始化方法
    def __init__(self, file_name, file_model, file_encoding):
        # 定义变量保存文件名和打开模式
        self.file_name = file_name
        self.file_model = file_model
        self.file_encoding = file_encoding

    # 上文方法
    def __enter__(self):
        print("进入上文方法")
        # 返回文件资源
        self.file = open(self.file_name, self.file_model)
        return self.file

    # 下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文方法")
        self.file.close()


if __name__ == '__main__':

    # 使用with管理文件
    with File("1.txt", "r", 'utf-8') as file:
        file_data = file.read()
        print(file_data)

