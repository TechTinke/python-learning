from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def listed_posts(request):
    listed_posts = Post.objects.all()
    return render(request, 'lost_and_found/listed_posts.html', {'listed_posts': listed_posts})

def post_detail(request, pk):
    post_details = Post.objects.get(pk=pk)
    return render(request, 'lost_and_found/post_detail.html', {'post_details': post_details})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Post.objects.create(title=title, description=description)
        return redirect('listed_posts')
    return render(request, 'lost_and_found/create_post_form.html')

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('listed_posts')

