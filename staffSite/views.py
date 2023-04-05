from tkinter import E
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from rest_framework import generics
from .serializers import OrderSerializers, StatusSerializers, OrderTypeSerializers

# Create your views here.

def menu(request):
    if request.user.is_superuser:
        order_list = Order.objects.all().order_by('created')
    else:
        order_list = Order.objects.filter(user = request.user.id).order_by('created')


    context = {
        'order_list':order_list,
    }
    return render(request, 'staffSite/menu.html', context)

def delete_order(request,pk):
    if request.user.is_superuser:
        order_list = Order.objects.all().order_by('created')
    else:
        order_list = Order.objects.filter(user = request.user.id).order_by('created')

    Order.objects.get(pk=pk).delete()
    
    context = {
        'order_list':order_list,
    }
    return redirect('menu')

def order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.user.is_superuser:
        order_list = Order.objects.all().order_by('created')
    else:
        order_list = Order.objects.filter(user = request.user.id).order_by('created')

    if request.POST:
        name = request.POST.get('name')
        second_name = request.POST.get('second_name')
        address = request.POST.get('address')
        order_type = request.POST.get('order_type')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Order.objects.filter(pk=pk).update(
            name=name,
            second_name =second_name,
            address = address,
            order_type =order_type,
            description =description,
            status = status,
            )
        order = Order.objects.get(pk=pk)

    for el in order_list:
        print(el.status.id)
    context = {
        'order_list':order_list,
        'order':order,
        'status':Status.objects.all(),
        'order_type':OrderType.objects.all(),
    }
    return render(request, 'staffSite/order.html', context)

# def my_order(request, pk):
#     if pk:
#         order = Order.objects.get(pk=pk)
#     else:
#         order = Order.objects.all(user = request.user.id).last()
    

#     context = {
#         'order_list':order_list,
#         'order':order,
#     }
#     return render(request, 'staffSite/order.html', context)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()

class OrderUserListView(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()


class OrderTypeListView(generics.ListAPIView):
    serializer_class = OrderTypeSerializers
    queryset = OrderType.objects.all()


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializers
    queryset = Status.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializers