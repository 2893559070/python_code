import multiprocessing
import time

# 定义全局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    # 代码执行到此，说明数据添加完成
    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)

# 提示:对应linux和mac主进程执行的代码不会进程接贝，但是对应window系统来说主进程执行的代码也会进行拷贝执行
# 对应window来说创建子进程的代码如果进程拷贝执行相当于递归无限制进行创建于进程，会报错

# 理解说明: 直接执行的模块就是主模块，那么直接执行的模块里面就应该添加判断是否是主模块的代码
# 1. 防止别人导入文件的时候执行主文件里面的代码
# 2. 防止windows系统递归创建子进程

if __name__ == '__main__':

    # 创建添加数据的子进程
    add_data_process = multiprocessing.Process(target=add_data)
    # 创建读取数据的子进程
    read_data_process = multiprocessing.Process(target=read_data)

    # 启动子进程执行对应的任务
    add_data_process.start()
    # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
    add_data_process.join()
    read_data_process.start()

    print("main:", g_list)

    # 总结: 多进程之间不共享全局变量

