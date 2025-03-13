from django.shortcuts import render
from django.http import HttpResponse

def check(request,id):
    if id % 2 != 0:
        return HttpResponse("odd")
    else:
        return HttpResponse("even")
    

# Create your views here.
