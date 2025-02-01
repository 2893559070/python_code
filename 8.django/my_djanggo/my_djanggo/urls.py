"""my_djanggo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''
1. urlpatterns 是固定写法，它的值是 列表
2. 我们在浏览器中输入的路径和会 urlpatterns中的每一项顺序进行匹配
    如果匹配成功，则直接引导到相应的模块
    如果匹配不成功，则返回404
    
3. urlpatterns中的元素是url
    url的一个参数是：正则
        r 转义
        ^ 严格的开始
        $ 严格的结尾
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
]
