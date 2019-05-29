from django.urls import path

from goods.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('goodlist/', goodlist, name='goodlist'),
    path('detail/', detail, name='detail'),
]