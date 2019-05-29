import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class UserLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            request.user = user.username
        # print(user)
        else:
            request.user = user_id            #往前端返回一个对象，用来渲染

        #中间件登录校验
        #过滤不需要做登录校验的地址
        path = request.path
        not_neet_login = ['/user/index','/user/login','/user/register','/user/logout', '/goods/goodlist','/goods/detail', '/carts/(.*)',
                          '/media/(.*)']
        for not_neet_path in not_neet_login:
            if re.match(not_neet_path, path):
                return None

        # if re.match ['/user/login/', '/user/register/', '/user/index/', '/carts/index/', '/goods/index/', '/goods/goodlist/','/goods/detail/', '/media/(.*)']:
        #     return None

        #登录校验
        user_id = request.session.get('user_id')
        if not user_id:
            return HttpResponseRedirect(reverse('user:login'))

        # return None
