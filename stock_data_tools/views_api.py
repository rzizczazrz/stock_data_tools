from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import *
from time import strftime, localtime

def login_api(request):
    context = {}
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    users = UserManagement.objects.filter(username=username).values()
    if len(users) == 0:
        context['code'] = 500
        context['msg'] = '不存在该用户'
    else:
        password_real = users[0]['password']
        if password != password_real:
            context['code'] = 500
            context['msg'] = '密码错误'
        else:
            user_id = users[0]['id']
            permission = UserManagement.objects.filter(id=user_id).values()[0]['permission']
            request.session['permission'] = permission
            request.session['username'] = username
            request.session['user_id'] = user_id
            context['code'] = 200
            context['msg'] = '登录成功'
    return JsonResponse(context)