from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.menu, name='menu'),
    path('order/<int:pk>/', views.order, name='order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    # path('my_order/<int:pk>/', views.my_order, name='my_order'),

    path('api/v1/status_all', views.StatusListView.as_view()),
    path('api/v1/order_all', views.OrderListView.as_view()),
    path('api/v1/order_type_all', views.OrderTypeListView.as_view()),
    path('api/v1/order_create', views.OrderCreateView.as_view()),



    # path('login_page/', views.login_page, name='login_page'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout_view, name='logout'),

    # path('api/my_orders/', views.OrderListViewUser.as_view()),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
