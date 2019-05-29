from django.shortcuts import render

# Create your views here.
from utils.functions import session_login


# @session_login
def index(request):
    if request.method == 'GET':

        return render(request, 'cart.html')