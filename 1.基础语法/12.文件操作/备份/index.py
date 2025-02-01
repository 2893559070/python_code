file1 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index.text', 'r')
file2 = open('C:\\学习\\后端\\python\\code\\基础语法\\12.文件操作\\index1.text', 'w')

while True:
    line = file1.read(1024)
    num = len(line)
    if num == 0:
        break;
    file2.write(line)

file1.close()
file2.close()

