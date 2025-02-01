from django.shortcuts import render
from .models import BookInfo, PeopleInfo
from django.http import HttpRequest, HttpResponse

# Create your views here.

'''
视图
1. 就是pythin函数
2. 函数的第一个参数就是 请求
    HttpRequest的实例对象
3. 返回一个响应
    HttpResponse的实例对象或者子类的实例对象
'''

# 数据操作
def index(request):
    name = '如花'

    books = BookInfo.objects.all()

    print(books, 'books')

    # 设置字典
    context = {
        'name': name,
        'books': books
    }

    response = render(request, 'index.html', context)
    # return HttpResponse('我是book的index页面')
    return response
    pass


###################新增数据#####################
# 新增方式1
book = BookInfo(
     name='python入门',
     pub_date='2010-1-1'
)
book.save()

# 新增方式二
PeopleInfo.objects.createo(
     name='zhangsan',
     book=book
)


###################修改数据#####################
PeopleInfo.objects.filter(name='zhangsan').update(name='张三')


###################删除数据#####################
# 删除方式1
person = PeopleInfo.objects.get(name='张三')
person.delete() # 返回 (1, {'book.PeopleInfo': 1})

# 删除方式2
BookInfo.objects.filter(name='python入门').delete() # 返回 (1, {'book.PeopleInfo': 1})


###################查询数据#####################
BookInfo.objects.get(id=1)  # 查询单个
BookInfo.objects.all()      # 查询全部
