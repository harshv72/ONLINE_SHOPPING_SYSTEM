from django.conf.urls import url
from buyapp.views import buy

urlpatterns= [
    url('^buy/$',buy),
]