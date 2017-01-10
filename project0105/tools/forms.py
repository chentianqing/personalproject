#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@Date      :   20170105
#@Author    :   chentianqing
#@email     :   993049884@qq.com
#@version   :   0.0.1

from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
