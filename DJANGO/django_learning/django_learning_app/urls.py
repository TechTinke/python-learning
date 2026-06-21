from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),# configure each URL, you add more URLs from here
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout, name='logout')
]