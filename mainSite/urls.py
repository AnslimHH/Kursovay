from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('make_order/', views.make_order, name='make_order'),
    path('my_order/', views.my_order, name='my_order'),

    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # path('api/my_orders/', views.OrderListViewUser.as_view()),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
