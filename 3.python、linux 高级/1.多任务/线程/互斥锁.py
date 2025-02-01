import threading

g_num = 0

# 创建锁
mutex = threading.Lock()

def task1():
    # 上锁
    mutex.acquire()
    for i in range(100):
        global g_num
        g_num += 1

    # 释放锁
    mutex.release()
    print(f'task1 {g_num}')

def task2():
    # 上锁
    mutex.acquire()
    for i in range(100):
        global g_num
        g_num += 1

    # 释放锁
    mutex.release()
    print(f'task2 {g_num}')

if __name__ == '__main__':
    task1_thread = threading.Thread(target=task1)
    task2_thread = threading.Thread(target=task2)

    task1_thread.start()
    task2_thread.start()

# 互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的数据没有问题
# 线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性，但是执行性能会下降
