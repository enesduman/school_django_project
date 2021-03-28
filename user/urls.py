
from django.contrib import admin
from django.urls import path

from . import views

app_name=("user")


urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/',views.loginUser, name="login" ),
    path('logout/',views.logoutUser, name="logout" ),
    path('dashboard/',views.dashboard, name="dashboard" ),
    path('register/<username>/edit/', views.register_detail, name='register_detail'),
]
