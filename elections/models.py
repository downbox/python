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

class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
        message = "%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname)
        return message
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
        message = "%s, %s 결혼했네" % (self.fullname, other.fullname)
        return message


class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))
