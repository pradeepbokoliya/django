from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Welcome to home page")

def login(request):
    return HttpResponse ("This is login page")

def signup(request):
    return HttpResponse("signup page under maintance")

def test(request):
    return HttpResponse("test page has been loaded smothly")


