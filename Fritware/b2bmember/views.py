from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from b2bmember.models import memberSignup
import random

# Create your views here.

# def member_login(request):
#     # third paramiter must be dict in rander function
#     pagedata = {'title':'My Member Login'}
    
#     return render(request, "b2bmember/login.html", pagedata)



def dt(request):
    return render(request, "b2bmember/dtlogin.html")

def rt(request):
    return render(request, "b2bmember/rtlogin.html")


def member_login(request):
    pagedata = {'title':'My Member Login'}
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        raw_password = request.POST.get('raw_password')

        data = User.objects.create_user(
            username = User(username = "fdsfsd"),
        
            email = email,
            password=raw_password,
            
        )
        
        User.save()
        
    return render(request,"b2bmember/login.html", pagedata)