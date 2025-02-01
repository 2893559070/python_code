import multiprocessing as mp

def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # 元组形式传参
    # sub_process = mp.Process(target=show_info, args=("李四", 20))

    # 字典形式传参
    sub_process = mp.Process(target=show_info, kwargs={"age": 20, "name": "王五"})

    sub_process.start()
    sub_process.join()


