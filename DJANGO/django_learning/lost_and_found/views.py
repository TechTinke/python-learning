from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def listed_posts(request):
    listed_posts = Post.objects.all() # getting all the posts that have been listed using the model Post
    return render(request, 'lost_and_found/listed_posts.html', {'listed_posts': listed_posts})


def post_detail(request, pk):
    post_details = Post.objects.get(pk=pk)
    return render(request, 'lost_and_found/post_detail.html', {'post_details': post_details})

def create_post(request):
    if not request.user.is_authenticated: #For an anonymous user, request.user.is_authenticated = False
        return redirect('login')
    
    #SHORTCUT VERSION
    # from django.contrib.auth.decorators import login_required

    # @login_required
    # def create_post(request):
    #     if request.method == 'POST':
    #         title = request.POST['title']
    #         description = request.POST['description']
    #         Post.objects.create(owner=request.user, title=title, description=description)
    #         return redirect('listed_posts')
    #     return render(request, 'lost_and_found/post_form.html')
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Post.objects.create(title=title, description=description)
        return redirect('listed_posts')
    return render(request, 'lost_and_found/create_post.html')


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if post.owner == request.user:
        post.delete()
    return redirect('listed_posts')


