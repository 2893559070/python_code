from django.db import models

# Create your models here.
'''
1. 定义模型
2. 模型迁移
    2.1 生成迁移文件
         python manage.py makemigrations
    2.2 在迁移（会在数据库中生成表，只会创建一个 数据表和模型的对应关系）
        python manage.py migrate
3. 操作数据库

4. ORM对应的关系
    表   <->    类
    字段  <->   属性
    
5. 模型类需要维承自models.Model
6. 模型类会自动为我们添加(生成)一个主键
    属性名:不要使用 python,mysql关键字
    不要使用 连续的下划线(__)

7. 书籍表
    id,name,pub date,readcount,commentcount,is_delete
'''

# 定义模型、模型继承
class BookInfo(models.Model):
    '''
        主键   当前会自动生成
        属性复制过来就可以
    '''
    name = models.CharField(max_length=10, unique=True)
    # 发布日期
    pub_date = models.DateTimeField('date published', null=True)
    # 阅读量
    readcount = models.IntegerField(default=0)
    # 评论量
    commentcount = models.IntegerField(default=0)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    # 修改表名
    class Meta:
        db_table = 'book_info'
        verbose_name = '书籍信息'

    def __str__(self):
        return self.name
    pass

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    # choices 设置字典
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # on_delete 设置级联删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书', default='')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'book_people'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
