from django.shortcuts import render,HttpResponseRedirect
from shoppingapp.models import Product,Cart
from django.template.context_processors import csrf

# Create your views here.
def cart_view(request):
    c={}
    c.update(csrf(request))
    if "uid" in request.session:
        uid = request.session.get('uid')
        cart = Cart.objects.filter(uid=uid)
        if cart:
            return render(request, 'cart.html', {'cart': cart})
        else:
            return HttpResponseRedirect('/shoppingapp/cate/')
    else:
        return HttpResponseRedirect('/shoppingapp/login/')

def cart(request):
    if "uid" in request.session:
        p_name = request.POST.get('pname', '')
        qty= request.POST.get('qty','')
        products=Product.objects.get(pname=p_name)
        pid = products.pid
        uid=request.session.get('uid')
        pname = products.pname
        image = products.image
        price = products.price
        cart=Cart.objects.filter(uid=uid)
        for c in cart:
            if c.pid==pid:
                qty=int(qty)+int(c.qty)
                Cart.objects.get(pid=pid).delete()

        cartob=Cart(uid=uid,pid=pid,pname=pname,price=price,image=image,qty=qty)
        cartob.save()
        cart = Cart.objects.filter(uid=uid)
        return render(request,'cart.html',{'cart':cart})
    else:
        return HttpResponseRedirect('/shoppingapp/login/')

def cart_add(request):
    if "uid" in request.session:
        p_name = request.POST.get('pname', '')
        qty= request.POST.get('qty','')
        products=Product.objects.get(pname=p_name)
        pid = products.pid
        uid=request.session.get('uid')
        pname = products.pname
        image = products.image
        price = products.price
        cart = Cart.objects.filter(uid=uid)
        for c in cart:
            if c.pid==pid:
                qty=int(qty)+int(c.qty)
                Cart.objects.get(pid=pid).delete()

        cartob=Cart(uid=uid,pid=pid,pname=pname,price=price,image=image,qty=qty)
        cartob.save()
        products=Product.objects.filter(cid=request.session.get('c_id'))
        return render(request,'product.html',{'products':products})
    else:
        return HttpResponseRedirect('/shoppingapp/login/')

def remove(request):
    c = {}
    c.update(csrf(request))
    cid=request.GET.get('cid','')
    cart=Cart.objects.get(pk=cid)
    uid = cart.uid
    cart.delete()
    cart = Cart.objects.filter(uid=uid)
    if cart:
        return render(request, 'cart.html', {'cart': cart})
    else:
        return HttpResponseRedirect('/shoppingapp/cate/')