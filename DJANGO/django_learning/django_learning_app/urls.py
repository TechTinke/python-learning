from django.urls import path
from . import views
#NB:
# - If URL refers to a specific object in your database, the URL Path 
# should describe the object you are referrring to and not the verb

# path('post/<str:pk>', views.post, name='post')

# - If URL refers to a standalone action with no associated object from database
# then the URL path can be named after the action

# path('register', views.register, name='register')

urlpatterns = [
    path('', views.index, name='index'),# configure each URL, you add more URLs from here
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout, name='logout'),
    path('counter', views.counter, name='counter'),
    path('post/<str:pk>', views.post, name='post') #string variable named pk
]   