import multiprocessing
import time

# 多进程的使用
# 导入进程包

# 跳舞任务
def dance():
    for i in range(10):
        print(f'跳舞中{i}')
        time.sleep(0.2)


# 唱歌任务
def sing():
    for i in range(10):
        print(f'唱歌中{i}')
        time.sleep(0.1)


# 创建子进程（自己手动创建的进程称之为子进程）
# 1. group 进程组 现在只能设置为None 一般不需要设置
# 2. target 进程执行的目标任务
# 3. name 进程名，如果不设置，默认为Process-1

if __name__ == '__main__':
    # 这里可以添加 freeze_support()，如果你打算将程序冻结为可执行文件
    # multiprocessing.freeze_support()  # 可选
    dance_process = multiprocessing.Process(target=dance)
    # 启动进程执行对应的任务
    dance_process.start()
    dance_process.join()

# 启动主进程
sing()

# 获取进程编号

# 进程执行带有参数的任务
