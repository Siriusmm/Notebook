import hashlib

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def index_views(request):
    if 'uname' in request.session or 'uname' in request.COOKIES:
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('/login')

def login_views(request):
    if request.method=='GET':
        if 'uname' in request.session or 'uname' in request.COOKIES:
            return render(request, 'index.html')
        else:
            return render(request,'login.html')
    else:
        uname=request.POST.get('uname',None)
        upassword=request.POST.get('upassword',None)
        pass

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        md=hashlib.md5()
        md.update(password.encode("utf-8"))
        pwd=md.hexdigest()
        User.objects.create(user_name=username,user_password=pwd)
        return HttpResponseRedirect('/login')

