from django.urls import path

from carts.views import *

urlpatterns = [
    path('index/',index,name='index'),

]