from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'school_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('order/',views.order,name='order'),
    path('logout/',views.home,name='logout')
]
