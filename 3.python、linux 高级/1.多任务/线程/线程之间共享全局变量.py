import threading

g_list = []

def add_data():
    for i in range(10):
        g_list.append(i)
        print("add: ", i)

    print("g_list添加数据完成")

def read_data():
    print(f"g_list: {g_list}")

if __name__ == '__main__':
    # 创建添加数据的子线程
    add_thread = threading.Thread(target=add_data)
    # 读取数据的线程
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    # join 当前线程（主线程）等待当前子线程执行完后在执行
    add_thread.join()
    read_thread.start()

