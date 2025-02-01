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
sql = "insert into students(name, birthday) values('赵六1', '2000-01-01')"
# sql = "delete from students where id=9"
# sql = "update students set name = '孙七' where id = 8"

try:
    # 3. 执行sql
    cur.execute(sql)
    # 3.1 提交数据
    conn.commit()
except Exception as e:
    # 3.2 回滚数据
    conn.rollback()
    print(e)
finally:
    # 4. 关闭游标
    cur.close()

    # 5. 关闭连接
    conn.close()
