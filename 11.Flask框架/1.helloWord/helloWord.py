# 导入Flask类
from flask import Flask
from core.config import DefaultConfig
from goods import goods_bp

# Flask类接收一个参数__name__
'''
import_name
    Flask程序所在的包(模块)，传 __name__ 就可以
    其可以决定 Flask 在访问静态文件时查找的路径
static_url_path
    静态文件访问路径，可以不传，默认为：/ + static_folder
static_folder
    静态文件存储的文件夹，可以不传，默认为 static
template_folder
    模板文件存储的文件夹，可以不传，默认为 templates
'''
app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static'
)

# 从配置对象中加载 Flask将配置信息保存到了app.config属性中，该属性可以按照字典类型进行操作。
# 读取 app.config.get(name) | app.config[name]
app.config.from_object(DefaultConfig)


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


# 在每一次请求之前调用，这时候已经有请求了，可能在这个方法里面做请求的校验
# 如果请求的校验不成功，可以直接在此方法中进行响应，直接return之后那么就不会执行视图函数
@app.before_request
def before_request():
    print("before_request")
    # if 请求不符合条件:
    #     return "laowang"


# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response


# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(response):
    print("teardown_request")

# 从配置文件中加载
# app.config.from_pyfile('setting.py')

# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    SECRET_KEY1 = app.config['SECRET1_KEY']
    return f'{SECRET_KEY1} Hello World'

# 在应用注册蓝图对象
app.register_blueprint(goods_bp, url_prefix='/goods')

@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    # app.run()
    app.run(host="127.0.0.1", port=5321, debug=True)
