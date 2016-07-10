#C\Code\mysite\elections\views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    cal1 = Calculator()
    cal2 = Calculator()
    pey = Service('영구')

    result = pey.sum(1,1)

    print("=== ",cal1.adder(3))
    print(cal1.adder(4))
    print(cal2.adder(3))
    result2 = cal2.adder(11)
    print(result2)
    print(type(result))

    return HttpResponse(result)
