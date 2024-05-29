from django.db import models

# Create your models here.
# Book model
class Book(models.Model):
    # 定义图书模型类
    title = models.CharField(max_length=100)  # 标题，最大长度100
    author = models.CharField(max_length=100)  # 作者，最大长度100
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 价格，最大整数位数10，小数位数2
    description = models.TextField()  # 描述

    def __str__(self):
        return self.title

