from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import requests

# Create your views here.

def home(request):

    context = {
        
    }
    return render(request, 'mainSite/home.html', context)

def make_order(request):
    response = requests.get('http://127.0.0.1:8000/staff/api/v1/status_all')
    status = response.json()

    response = requests.get('http://127.0.0.1:8000/staff/api/v1/order_type_all')
    order_type = response.json()

    if request.POST:
        user = request.user.id
        name = request.POST.get('name')
        second_name = request.POST.get('second_name')
        address = request.POST.get('address')
        order_type = request.POST.get('order_type')
        description = request.POST.get('description')

        response_type = requests.post('http://127.0.0.1:8000/staff/api/v1/order_create', data={
            'user': user,
            'name': name,
            'second_name': second_name,
            'address': address,
            'order_type': order_type,
            'status': 1,
            'description': description,
    
        })
        return redirect('home')

    context = {
        "status":status,
        "order_type":order_type,
    }
    return render(request, 'mainSite/make_order.html', context)



def my_order(request):
    response = requests.get('http://127.0.0.1:8000/staff/api/v1/order_all')
    order = response.json()

    response = requests.get('http://127.0.0.1:8000/staff/api/v1/status_all')
    status = response.json()
  
    response = requests.get('http://127.0.0.1:8000/staff/api/v1/order_type_all')
    order_type = response.json()

    context = {
        'order':order,
        'status':status,
        'order_type':order_type,
        
    }
    return render(request, 'mainSite/my_order.html', context)

def register(request):
    user_form = CreateUserForm

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
                user_form.save()
                username = request.POST.get('username')
                password = request.POST.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request,user)

                return redirect('home')

    context = {
        'user_form':user_form,
    }

    return render(request, 'mainSite/register.html', context)



def login_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error = 'Проверьте введёные данные!'

    context = {
        "error":error,

    }
    return render(request, 'mainSite/login.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')