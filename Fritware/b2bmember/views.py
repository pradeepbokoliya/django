from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def member_login(request):
    # third paramiter must be dict in rander function
    pagedata = {'title':'My Member Login'}
    
    return render(request, "b2bmember/login.html", pagedata)



def dt(request):
    return render(request, "b2bmember/dtlogin.html")

def rt(request):
    return render(request, "b2bmember/rtlogin.html")
