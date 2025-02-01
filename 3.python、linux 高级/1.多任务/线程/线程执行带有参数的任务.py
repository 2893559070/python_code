import threading
import time

def sub_thread(name, age):
    print(f"name: {name}, age: {age}")

if __name__ == '__main__':
    # 创建子线程
    sub_thread = threading.Thread(target=sub_thread, args=('李四', 20))
    # 启动线程
    sub_thread.start()

