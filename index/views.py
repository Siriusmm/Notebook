from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index_views(request):
    if 'uname' in request.session or 'uname' in request.COOKIES:
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('/login/')

def login_views(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        pass

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        pass
