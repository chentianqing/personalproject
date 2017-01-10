#!/usr/bin/env python
#_*_ coding:    utf-8 _*_
#Date   :   2017-1-05
#Author :   chentianqing(993049884@qq.com)
#version:   0.0.1

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



############################
# 与上述代码无关联。其它测试代码。
############################

class Article2(models.Model):
    title = models.CharField(u'标题',max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)

    def __str__(self):
        return self.title