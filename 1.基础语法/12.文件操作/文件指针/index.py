"""
    seek 偏移量，起始位置
        起始位置
            0   文件开头
            1   当前位置
            2   文件结尾

    mode：r 一起使用
"""

file1 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text', 'r')

file1.seek(2, 0)
text1 = file1.read()

print(text1)

file1.close()

