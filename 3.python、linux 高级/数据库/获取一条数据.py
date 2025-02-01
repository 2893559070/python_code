import pymysql


# 1. 创建连接对象
conn = pymysql.connect(host="192.168.37.222",
                       port=3306,
                       user="zihan01",
                       passwd="root",
                       database="test01",
                       charset='utf8')

# 2. 获取游标，执行sql语句
cur = conn.cursor()

# 2.1 准备sql
sql = "select * from students"

# 3. 执行sql
cur.execute(sql)

# 3.1 获取查询结果 返回的数据类型是一个元组
row = cur.fetchone()
print(row)

# 4. 关闭游标
cur.close()

# 5. 关闭连接
conn.close()
