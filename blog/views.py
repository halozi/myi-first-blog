from django.shortcuts import render#导入render模块

#先定义一个数据列表，当然后面熟了可以从数据库里取出来
list = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]

def index(request):

    return render(request,'k.html',{'form':list})#通过render模块把index.html这个文件返回到前端，并且返回给了前端一个变量form，在写html时可以调用这个form来展示list里的内容
