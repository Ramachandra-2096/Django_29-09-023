from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    msg ='<h1>Hello there..!<\h1>'
    return HttpResponse(msg)
