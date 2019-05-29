from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from goods.models import liulan
from user.form import UserForm, LoginForm
from user.models import User
# from utils.functions import session_login


# @session_login
def index(request):
    return render(request, 'index.html')

#登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 到这里字段表单里字段正确，且数据库里有此用户名
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)

            #校验密码是否一致
            if not check_password(password, user.password):
                pwd_error = '密码错误'
                return render(request, 'login.html', {'pwd_error': pwd_error})
            #密码通过
            res = HttpResponseRedirect(reverse('user:index'))
            #设置缓存，session
            request.session['user_id'] = user.id
            return res

        errors = form.errors
        return render(request,'login.html', {'errors': errors})



#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        #表单校验
        form = UserForm(request.POST)
        if form.is_valid():
            #表单校验成功
            username = form.cleaned_data.get('username')
            password = make_password(form.cleaned_data.get('pwd1'))
            email = form.cleaned_data.get('email')
            User.objects.create(username=username,password=password,email=email)

            #重定向登录页面
            return HttpResponseRedirect(reverse('user:login'))

    errors = form.errors
    return render(request, 'register.html',{'errors':errors})

#用户中心
# @session_login
def UserCenter(request):
    if request.method == 'GET':
        gs = liulan.objects.all()
        return render(request, 'user_center_info.html',{'gs':gs})

#注销
def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return HttpResponseRedirect(reverse('user:login'))


