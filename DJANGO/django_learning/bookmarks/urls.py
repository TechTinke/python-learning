from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #gateway for bookmarks app(login)
    path('saved_links', views.saved_links, name='saved_links'),
    path('create_link', views.create_link, name='create_link'),
    path('link/<str:pk>', views.link_detail, name='link_detail'),
    path('link/<str:pk/update', views.link_update, name='link_update')
]