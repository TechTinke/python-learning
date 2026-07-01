from django.urls import path
from . import views

#NB:
# - URL names in Django live in one flat, project wide lookup table and
# doesn't care what app is being pointed to
# - That means a view from django_learning_app could be used in the bookmarks apps 
# unless there is redirection that is app specific

urlpatterns = [
    path('', views.login, name='login'), #gateway for bookmarks app(login)
    path('saved_links', views.saved_links, name='saved_links'),
    path('create_link', views.create_link, name='create_link'),
    path('link/<str:pk>', views.link_detail, name='link_detail'),
    path('link/<str:pk/update', views.link_update, name='link_update')
]