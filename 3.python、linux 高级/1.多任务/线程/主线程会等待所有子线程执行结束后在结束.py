import threading
import time

def task():
    while True:
        print("任务执行中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 设置守护主线程 daemon=True 主线程退出子线程销毁
    sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread.start()

    # 主线程延时执行1秒
    time.sleep(1)

    print("over")
    exit()
