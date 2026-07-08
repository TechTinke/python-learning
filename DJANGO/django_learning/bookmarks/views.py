from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Link
from django.contrib.auth.decorators import login_required

# Create your views here.
# NB:
# Bookmarks and django_learning_app are 2 apps living in the same django_project
# - Same authentication system
# - One database
# - One django_session table
# - One user table

# When auth.login(request, user) runs, Django creates a row in the django_sesson table
# and sends your browser a cookie(sessionid) - contains the key to that row.
# Cookies are scoped to a domain + port e.g 127.0.0.1:8000 and on every request after that,
# browser automatically sends back that cookie to the server

# Cookies - small text files website saves on your device and they help browsers remember your login details
# language preferences, shopping cart items ensuring a personalized and seamless experience
# HOW COOKIES WORK
# When you visit a website, its server sends a cookie to your web browser which then stores it
# on your device's hard drive and every time you return to that site, your web browser sends back the cookie
# to the server allowing the website to recognize you and load your customized settings


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password) #returns None is the user isn't authenticated
        if user is not None:
            auth.login(request, user)
            return redirect('saved_links')
        else:
            messages.info(request, 'OOPS! Your login credentials could not be found')
            return redirect('/bookmarks')
    return render(request, 'bookmarks/login.html')
@login_required #when @login_required redirects an unauthenticated user, it doesn't just send them to LOGIN_URL,
#it appends where they wanted to go as a query parameter(?next=/bookmarks/saved_links)
def saved_links(request):
    # NB:
    # - Since everything else is implicitly behind the login,
    # every view except login needs the same gate of authentication
    # if not request.user.is_authenticated:
    #     messages.info(request, "You need to log in first")
    #     return redirect('/bookmarks')
    # saved_links = Link.objects.all() #all returns all rows(url, details) - no conditions
    saved_links = Link.objects.filter(link_owner=request.user) #filter() - filters by a certain condition
    return render(request, 'bookmarks/saved_links.html', {'saved_links': saved_links})
def create_link(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in first")
        return redirect('/bookmarks')
    if request.method == 'POST':
        url = request.POST['url']
        details = request.POST['details']
        Link.objects.create(link_owner=request.user, url=url, details=details)
        return redirect('saved_links')
    return render(request, 'bookmarks/create_link.html')
def update_link(request, pk):
# HTML Forms can only ever submit GET or POST methods so the other methods(PUT, DELETE & QUERY)
# cannot be submitted via a form1
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('/bookmarks')
    link_details = Link.objects.get(pk=pk)
    if request.method == 'POST':
        # We use link_details.url and link_details.details to put
        # the values pulled out of the post data onto link_details
        link_details.url = request.POST['url'] 
        link_details.details = request.POST['details']
        link_details.save() #writes the object's attribute values to the database
        return redirect('saved_links')
    return render(request, 'bookmarks/update_link.html', {'link_details': link_details})
def link_detail(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('/bookmarks')
    link_details = Link.objects.get(pk=pk)
    return render(request, 'bookmarks/link_detail.html', {'link_details': link_details})