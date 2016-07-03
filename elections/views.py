#C\Code\mysite\elections\views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculator

def index(request):
    cal1 = Calculator()
    cal2 = Calculator()

    print(cal1.adder(3))
    print(cal1.adder(4))
    print(cal2.adder(3))
    print(cal2.adder(11))

    return HttpResponse(cal2.adder(11))
