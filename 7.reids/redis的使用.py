# 导入redis
import redis

if __name__ == '__main__':
    # 创建redis的连接实例
    try:
        rs = redis.Redis(host='192.168.37.222', port=6379)

        rs.set('name', 'zhangsan')

        name = rs.get('name')

        print(rs)
        print(f'name : {name}')

    except Exception as e:
        print(e)
    finally:
        rs.close()
