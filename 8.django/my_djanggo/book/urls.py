from django.urls import path, include
from . import views

urlpatterns = [
    # index/
    # url的第一参数是:正则
    # url的第二参数是:视图函数名
    path('index/', views.index),
]
