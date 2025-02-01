# 在这种情况下,Python提供了 with 语句的这种写法，既简单又安全，
# 并且 with 语句执行完成以后自动调用关闭文件操作，即使出现异常也会自动调用关闭文件操作。
# 1、以写的方式打开文件
with open("1.txt", "w") as f:
    # 2、读取文件内容
    f.write("hello world")