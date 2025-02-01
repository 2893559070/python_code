import threading

g_num = 0

def task1():
    for i in range(100):
        global g_num
        g_num += 1

    print(f'task1 {g_num}')

def task2():
    for i in range(100):
        global g_num
        g_num += 1

    print(f'task2 {g_num}')

if __name__ == '__main__':
    task1_thread = threading.Thread(target=task1)
    task2_thread = threading.Thread(target=task2)

    task1_thread.start()
    # 使用线程等待处理全局数据处理错误
    task1_thread.join()
    task2_thread.start()
