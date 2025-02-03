from flask import Blueprint

goods_bp = Blueprint('goods', __name__)

# 注意 Blueprint 实例 与视图的引用先后，避免循环引用
from . import views
