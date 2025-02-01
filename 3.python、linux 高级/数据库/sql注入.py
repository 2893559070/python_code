import pymysql

# sql注入会导致数据泄露

# 1. 创建连接对象
conn = pymysql.connect(host="192.168.37.222",
                       port=3306,
                       user="zihan01",
                       passwd="root",
                       database="test01",
                       charset='utf8')

# 2. 获取游标，执行sql语句
cur = conn.cursor()

# 使用参数化 防止注入
# params = (8,)
params = ['赵六1', '2000-01-01']

# 2.1 准备sql
# sql = "select * from students where id = %s"
sql = "insert into students(name, birthday) values(%s, %s)"

try:
    # 3. 执行sql
    cur.execute(sql, params)

    # rows = cur.fetchall()
    # print(rows)

    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
finally:
    # 4. 关闭游标
    cur.close()

    # 5. 关闭连接
    conn.close()
