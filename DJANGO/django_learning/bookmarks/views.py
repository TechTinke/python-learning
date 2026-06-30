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
            return redirect('/bookmarks')
    return render(request, 'bookmarks/login.html')
def saved_links(request):
    saved_links = Link.objects.all()
    return render(request, 'bookmarks/saved_links.html', {'saved_links': saved_links})
def create_link(request):
    if request.method == 'POST':
        url = request.POST['url']
        details = request.POST['details']
        Link.objects.create(url=url, details=details)
        return redirect('/saved_links')
    return render(request, 'bookmarks/create_link.html')
def link_update(request, pk):
    link_details = Link.objects.get(pk=pk)
    if request.method == 'PATCH':
        url = request.PATCH['title']
        details = request.PATCH['description']
        Link.objects.update(url=url, details=details)
        return redirect('/saved_links')
    return render(request, 'bookmarks/update_link.html', {'link_details': link_details})
def link_detail(request, pk):
    link_details = Link.objects.get(pk=pk)
    return render(request, 'bookmarks/link_detail.html', {'link_details': link_details})