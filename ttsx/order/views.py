from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from order.form import addressForm
from order.models import UserAddress
from user.models import User

from utils.functions import session_login


# @session_login
def index(request):
    if request.method == 'GET':
        user_address = UserAddress.objects.all()
        # print(user_address)
        return render(request, 'user_center_site.html',{'add':user_address})
    if request.method == 'POST':
        form = addressForm(request.POST)
        if form.is_valid():
            #输入正确
            filename = form.cleaned_data['filename']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            number = form.cleaned_data['number']
            UserAddress.objects.create(user=filename, address=address, signer_postcode=zipcode, signer_mobile=number)

            return HttpResponseRedirect(reverse('order:index'))
        errors = form.errors
        return render(request,'user_center_site.html',{'errors':errors})