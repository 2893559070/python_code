# 1. 导入线程模块
import threading
import time

def sing():
    # 获取当前子线程
    sing_thread = threading.current_thread()
    print("sing_thread: ", sing_thread)
    for i in range(10):
        print(f' {i} ：唱歌中')
        time.sleep(0.1)

def dance():
    # 获取当前子线程
    dance_thread = threading.current_thread()
    print("dance_thread: ", dance_thread)
    for i in range(10):
        print(f' {i} ：跳舞中')
        time.sleep(0.1)

if __name__ == '__main__':
    # 获取当前主线程
    main_thread = threading.current_thread()
    print("main_thread: ", main_thread)

    # 2. 创建子线程
    sing_thread = threading.Thread(target=sing, name="sing_thread")
    dance_thread = threading.Thread(target=dance, name="dance_thread")

    # 3. 启动子线程
    sing_thread.start()
    dance_thread.start()



