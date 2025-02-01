# read

file1 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text')
file2 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text')
file3 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text')

# 读取全部
text1 = file1.read()
print(text1, 'text1')

# 一次读取多行
text2 = file2.readlines()
print(text2, 'text2')

# 一次读取一行
text3 = file3.readline()
print(text3, 'text3')


file1.close()
