from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from .models import *
import json
from django.db.models import Q

@csrf_exempt
def login(request):
    context = {}
    return render(request, 'login.html', context=context)

@csrf_exempt
def index(request):
    context = {}

    context = fill_session(request, context)
    return render(request, 'index.html', context=context)