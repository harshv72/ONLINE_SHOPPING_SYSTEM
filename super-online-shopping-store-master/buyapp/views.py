from django.shortcuts import render,HttpResponseRedirect
from django.template import context

from shoppingapp.models import Cart
# Create your views here.

def buy(request):
    if "uid" in request.session:
        uid=request.session.get('uid')
        products=Cart.objects.filter(uid=uid)
        total=0
        for p in products:
            total=total+(p.qty*p.price)
        context={'products':products,'total':total}
        Cart.objects.filter(uid=uid).delete()
        return render(request,'billf.html',context)
    else:
        return HttpResponseRedirect('/shoppingapp/login/')
