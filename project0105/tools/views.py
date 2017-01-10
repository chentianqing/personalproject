#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@Date      :   20170105
#@Author    :   chentianqing
#@email     :   993049884@qq.com
#@version   :   0.0.1

from django.shortcuts import render
from django.http import HttpResponse

#引入表单类
from .forms import AddForm

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST) #form 包含提交的数据

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:   #正常访问
        form = AddForm()
    return render(request,'index.html',{'form':form})


