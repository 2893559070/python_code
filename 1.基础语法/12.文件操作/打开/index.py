"""
    open
        name: 文件名 及 文件所在的路径
        mode: 设置打开文件的模式 默认为a
            读 写 追加
            r 只读，文件不存在则报错
            w 只写，文件不存在则创建
            a 追加, 文件不存在则创建
            r+  文件指针在开头，可以读取出数据，文化不存在则报错
            w+ 文件指针在开头 新内容会覆盖原内容
"""
file1 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text', 'a')

file1.write('aaa')

file1.close()
