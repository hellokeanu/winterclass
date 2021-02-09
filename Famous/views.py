from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("Hello")
    return HttpResponse("Hello")