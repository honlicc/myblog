from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
import re
from user.models import User
from blog.settings import SECRET_KEY
from celery_tasks.tasks import send_register_active_email


# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 接收参数
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        email = request.POST.get('email')

        # 合法性校验
        if pwd != pwd2:
            return render(request, 'register.html', {'errmsg': '两次密码输入不一致，请重新输入'})

        if not all([username, pwd, email]):
            return render(request, 'register.html', {'errmsg': '信息填写不完整，请重新输入'})

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确，请重新输入'})

        # 业务逻辑处理
        # 判断用户是否已存在
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户已存在，请重新输入'})

        user = User.objects.create_user(username=username, email=email, password=pwd)
        user.is_active = 0
        user.save()

        # 生成token
        serializer = Serializer(SECRET_KEY, 60 * 10)
        info = {"user_id": user.id}
        token = serializer.dumps(info).decode()

        # 发送邮件让用户激活
        send_register_active_email.delay(email, username, token)

        # 返回应答
        return redirect(reverse('home:index'))


# 用户激活
class ActivateView(View):
    def get(self, request, token):
        serializer = Serializer(SECRET_KEY, 60 * 10)
        try:
            info = serializer.loads(token)
            user = info['user_id']
            user = User.objects.get(id=user)
            user.is_active = 1
            user.save()
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            return HttpResponse("激活连接已过期")


class LoginView(View):
    def get(self, request):
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'login.html', {'username': username})

    def post(self, request):
        # 接收参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 参数校验
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '信息填写不完整，请重新输入'})

        # 业务逻辑处理

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if not user:
            return render(request, 'login.html', {'errmsg': '用户或密码错误'})

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                # 获取登录后所需要跳转的页面
                nest_url = request.GET.get('next', reverse("home:index"))
                response = redirect(nest_url)

                response.set_cookie('username', username, max_age=3600 * 24)

                return response

            else:

                # 生成token
                serializer = Serializer(SECRET_KEY, 60 * 10)
                info = {"user_id": user.id}
                token = serializer.dumps(info).decode()
                email = user.email

                # 发送邮件让用户激活
                send_register_active_email.delay(email, username, token)
                return render(request, 'login.html', {'errmsg': '账户未激活,请重新激活'})
        else:
            return render(request, 'login.html', {'errmsg': '用户或密码错误'})

        # 返回应答


# /user/loginout
class LoginOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home:index'))
