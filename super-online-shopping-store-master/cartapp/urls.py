from django.conf.urls import url
from cartapp.views import cart,remove,cart_add,cart_view

urlpatterns= [
    url('^cart/$',cart),
    url('^cart_add/$',cart_add),
    url('^cart_view/$',cart_view,name='cart'),
    url('^remove/$',remove),
]