from django.urls import path
from . import views

urlpatterns = [
    path('', views.listed_posts, name='listed_posts'), # gateway for lost_and_found
    path('create_post', views.create_post, name='create_post'),
    path('post/<str:pk>', views.post_detail, name='post_detail'), # post/<str:pk> - points to the particular object(post)
    path('post/<str:pk>/delete', views.delete_post, name='delete_post' )
]