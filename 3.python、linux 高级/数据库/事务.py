import pymysql

# 只要使用事务，表中的数据都是合法的数据，不是垃圾数据
# 存储引擎 InnoDb 才支持事务，mysql默认是InnoDb存储引擎
# 存储引擎 MyISAM 不支持事务，查询快
# pymysql 默认开启事务

"""
事务的特性:
    原子性: 强调事务中的多个操作时一个整体
    一致性: 强调数据库中不会保存不一致状态
    隔离性: 强调数据库中事务之间相互不可见
    持久性: 强调数据库能永久保存数据，一旦提交就不可撤销

MySQL数据库默认采用自动提交(autocommit)模式, 
也就是说修改数据(insert、update、delete)的操作会自动的触发事务,
完成事务的提交或者回滚
    开启事务使用 begin 或者 start transaction;
    回滚事务使用 rollback;
    pymysql 里面的 conn.commit() 操作就是提交事务
    pymysql 里面的 conn.rollback() 操作就是回滚事务
"""