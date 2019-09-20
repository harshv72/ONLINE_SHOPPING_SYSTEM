from django.conf.urls import url,include
from shoppingapp.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$',index),
    url(r'^login/$',login,name='login'),
    url('^cart_view/$',cart_view,name='cart'),
    url('^signup/$',signup,name='signup'),
    url('^adduserinfo/$',adduserinfo),
    url('^getuserinfo/$', getuserinfo),
    url('^forgot/$', forgot),
    url('^cate/$', cate),
    url('^about/$',about),
    url('^contact/$', contact),
    url('^contact2/$', contact2),
    url(r'^product/$',product),
    url(r'^auth/$',auth_view),
    url(r'^auth_forgot/$', auth_view_forgot),
    url(r'^logout/$',logout,name='logout'),
    url(r'^invalidlogin/$',invalidlogin),
    url(r'^invalidpassword/$', invalidpassword),
    url(r'^newpassword/$', newpassword),
]
