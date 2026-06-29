from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Link
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('saved_links')
        else:
            messages.info(request, 'OOPS! Your login credentials could not be found')
            return redirect('/')
    return render(request, 'bookmarks/login.html')
def saved_links(request):
    saved_links = Link.objects.all()
    return render(request, 'bookmarks/saved_links.html', {'saved_links': saved_links})
def create_link(request):
    return render(request, 'bookmarks/create_link.html')
def link_update(request, pk):
    return render(request, 'bookmarks/update_link.html', {'pk': pk})
def link_detail(request, pk):
    return render(request, 'bookmarks/link_detail.html', {'pk': pk})