from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from b2bmember.models import memberSignup
import random
from .forms import SignupForm


def dt(request):
    return render(request, "b2bmember/dtlogin.html")

def rt(request):
    return render(request, "b2bmember/rtlogin.html")


def member_login(request):
    form = SignupForm()
    title = "Member Login"
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request,"b2bmember/login.html", {'form':form, 'title' : title})

# def user_login(request):
#     if request.method == "POST":
#         fm = SignupForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = SignupForm()
#     return render(request,"b2bmember/test.html", {'form':fm})