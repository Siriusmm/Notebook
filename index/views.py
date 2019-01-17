import hashlib
import json

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
            result=''
            return render(request,'login.html')
    else:
        uname=request.POST.get('uname',None)
        upassword=request.POST.get('upassword',None)
        upwd=md=hashlib.md5()
        md.update(upassword.encode("utf-8"))
        pwd=md.hexdigest()
        user=User.objects.filter(user_name=uname,user_password=pwd)
        if user:
            request.session["uname"]=uname
            resp = HttpResponseRedirect("/")
            if "remember_password" in request.POST:
                resp.set_cookie("uname","uname",3600*24*365)
            return resp
        else:
            result="用户名或密码错误"
            return render(request,"login.html",locals())

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else :
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        avatar=request.FILES.get("avatar","")
        if avatar:
            avatar_name = username + "." + avatar.name.split(".")[-1]
            with open("upload/avatar/"+avatar_name, "wb") as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
        else:
            avatar=None
        if username and password:
            md=hashlib.md5()
            md.update(password.encode("utf-8"))
            pwd=md.hexdigest()
            User.objects.create(user_name=username,user_password=pwd,user_avatar=avatar_name)
            return HttpResponseRedirect('/login/')

def check_views(request):
    user_name=request.GET.get("username")
    print(user_name)
    user=User.objects.filter(user_name=user_name).values()
    print(user)
    if user:
        d=dict(msg="no-ok")
        print(d)
    else:
        d=dict(msg="ok")
        print(d)
    return HttpResponse(json.dumps(d), content_type="application/json")

def test_views(request):
    user = User.objects.filter(user_name="wwww").values()
    print("user------------->",user)
    users=User.objects.all().values()
    print("users------------->",users[0])
    return HttpResponse("OK")



