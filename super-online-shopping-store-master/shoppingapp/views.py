from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, request
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from shoppingapp import models
from shoppingapp.models import Product

def index(request):
    return render(request,'index.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        request.session['uid']=request.user.id
        return HttpResponseRedirect('/shoppingapp/cate/')
    else:
        return HttpResponseRedirect('/shoppingapp/invalidlogin/')

def auth_view_forgot(request):
    username = request.POST.get('uname','')
    email = request.POST.get('email','')
    user = auth.authenticate(username=username,email=email)
    if user:
        return HttpResponseRedirect('/shoppingapp/newpassword/')
    else:
        return HttpResponseRedirect('/shoppingapp/invalidpassword/')

def signup(request):
    c={}
    c.update(csrf(request))
    return render(request,'signup.html',c)


def adduserinfo(request):
    uname=request.POST.get('username','')
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    cpassword=request.POST.get('pass2','')
    if(password==cpassword):
        user=User(username=uname,password=make_password(password),email=email)
        user.save()
        return auth_view(request)
    else:
        return render(request,'signup.html',{"error":"password doesn't match"})

def getuserinfo(request):
    uname=request.POST.get('name','')
    password=request.POST.get('pass','')
    user=models.User.objects.filter(username=uname,password=password)
    data={'data':user}
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def contact2(request):
    return render(request,'contact2.html')

def invalidpassword(request):
    return render(request,'invalidpassword.html')

def newpassword(request):
    return render(request,'newpassword.html')

def forgot(request):
    c = {}
    c.update(csrf(request))
    return render(request,'forgot.html',c)

def cate(request):
    return render(request,'category.html')

def product(request):
    c = {}
    c.update(csrf(request))
    cid=request.GET.get('cid')
    request.session['c_id']=cid
    products=Product.objects.filter(cid=cid)

    return render(request,'product.html',{'products':products},c)

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def cart_view(request):
    uid = request.session.get('uid')
    cart = Cart.objects.filter(uid=uid)
    return render(request, 'cart.html', {'cart': cart})
