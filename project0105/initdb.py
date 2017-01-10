#!/usr/bin/env python
#_*_ coding:   utf-8 _*_
#@Date      :   20170105
#@Author    :   chentianqing(993049884@qq.com)
#@Link      :
#@version   :   0.0.1

from __future__ import unicode_literals
from project0105.wsgi import *
from blog.models import Author,Article,Tag
import random

author_name_list = ['chentianqing','chentq','chenm','chenmin']
article_title_list = ['Django教程','python教程','HTML教程','JAVA教程']

def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1,3))
        author.email = '%s@ziqiangxuetang.com' % (author.addr)
        author.save()


def create_articles_and_tags():
    #文章随机生成
    for article_title in article_title_list:
        tag_name = article_title.split(' ',1)[0]
        tag,created = Tag.objects.get_or_create(name=tag_name)
        random_author = random.choice(Author.objects.all())

        for i in range(1,21):
            title = '%s_%s' % (article_title,i)
            article, created = Article.objects.get_or_create(
                title = title,defaults={
                    'author':   random_author,
                    'content':  '{} 正文'.format(title),
                    'score':    random.randrange(70,100)
                    }
            )
            article.tags.add(tag)


def main():
    create_authors()
    create_articles_and_tags()


if __name__ == "__main__":
    main()
    print('good ! welldone . come on !')