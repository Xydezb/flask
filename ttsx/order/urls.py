from django.urls import path

from order.views import *

urlpatterns = [
    path('index/', index, name='index'),

]