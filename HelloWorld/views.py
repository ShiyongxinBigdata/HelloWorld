from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    """ 访问首页 """
    # 渲染页面：
    return render(request, 'index.html')

def login_view(request):
    """ 登录功能 """
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 获取请求参数：
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 判断
        if uname == 'zhangsan' and pwd == '123':
            return HttpResponse(f'{uname}, 欢迎登录！')
        else:
            return render(request, 'login.html')
    else:
        return HttpResponse('您走错了！')

def test():
    print()