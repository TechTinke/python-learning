from django.urls import path
from . import views

urlpatterns = [
    path('listed_posts', views.listed_posts, name='listed_posts'),
    path('create_post', views.create_post, name='create_post'),
    path('post_detail<str:pk>', views.post_detail, name='post_detail'),
    path('delete_post<str:pk>', views.delete_post, name='delete_post' )
]