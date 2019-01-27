import hashlib
import json

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def index_views(request):
    if request.method=='GET':
        user_name = request.session.get("uname","")
        if not user_name:
            user_name = request.COOKIES.get("uname","")
        print(user_name)
        if user_name:
            user=User.objects.filter(user_name=user_name)[0]
            notes=user.notes_set.all()
            return render(request,'index.html',locals())
        else:
            return HttpResponseRedirect('/login')
    else:
        user_name = request.session.get("uname", "")
        if not user_name:
            user_name = request.COOKIES.get("uname", "")
        print(user_name)
        title=request.POST.get("title",'')
        print(title)
        content=request.POST.get("notes",'')
        print(content)
        Notes.objects.create(notes_title=title,note_content=content,notes_user_name=User.objects.get(user_name=user_name))
        return HttpResponse("插入成功")
def user_views(request,user):
    username=user
    print(username)
    user_name = request.session.get("uname", "")
    print("session----------->",user_name)
    if not user_name:
        user_name = request.COOKIES.get("uname", "")
    if user_name==username:
        user=User.objects.filter(user_name=user)[0]
        return render(request,'info.html',locals())
    else:
        return HttpResponseRedirect("/login/")

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
                resp.set_cookie("uname",uname,3600*24*365)
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
            with open("index/static/images/avatar/"+avatar_name, "wb") as f:
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
def showcontent(request,id):
    note=Notes.objects.filter(id=id)[0]
    print("title------------>",note.notes_title)
    return HttpResponse(note.note_content)

def test_views(request):
    # d=dict(notes_user_name=User.objects.get(id=1),notes_title="赌圣",note_content="今晚打老虎")
    # Notes.objects.create(**d)
    # user=User.objects.get(user_name="www")
    # notesSet=user.notes_set.all()
    # for i in notesSet:
    #     print(i.note_content)
    # notes=Notes.objects.get(id=1)
    # user=notes.notes_user_name
    # print(user.user_name,user.id,user.user_email)
    User.objects.filter(id=1).delete()

    return  HttpResponse("get")



