#C\Code\mysite\elections\views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    cal1 = Calculator()
    cal2 = Calculator()
    pey = Service('영구')

    result = pey.sum(1,1)

    #print("=== ",cal1.adder(3))
    #print(cal1.adder(4))
    #print(cal2.adder(3))
    #result2 = cal2.adder(11)
    #print(result2)
    #print(type(result))

    # 상속 예시
    pey = HousePark('응용')
    juliet = HouseKim('줄리엣')
    result = pey.love(juliet)
    result1 = pey + juliet

    return HttpResponse(result + '<br>' + result1)