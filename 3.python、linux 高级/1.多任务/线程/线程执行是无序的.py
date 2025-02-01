import threading

def task():
    # 获取当前线程
    print(threading.current_thread().name)

if __name__ == '__main__':
    for i in range(10):
        # 线程、进程 之间执行是无序的，具体那个线程执行是由cpU调度绝定的
        sub_thread = threading.Thread(target=task, name=f'Thread{i}')
        sub_thread.start()
