from django.db import models
from django.http import HttpResponse

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

class Service:
    secret = "영구는 배꼽이 두 개다"
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        message = "%s님 %s + %s = %s입니다." % (self.name, a, b, result)
        return message
