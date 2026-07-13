from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Entry
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('journal_entries')
        else:
            messages.info(request, "OOPS!Your login credentials could not be found")
            return redirect('/bookmarks')
    return render(request, 'journal/login.html')
@login_required
def journal_entries(request):
    journal_entries = Entry.objects.filter(entry_owner=request.user)
    # if journal_entries is None: #Entry.objects.filter never returns None even if there are no results, it returns an empty QuerySet
    #     messages.info(request, "You do not have any Journals yet, create one below:")
    if not journal_entries.exists():
        messages.info(request, "You do not have any Journals yet, create one below:")
    return render(request, 'journal/journal_entries.html', {'journal_entries': journal_entries})
@login_required
def create_entry(request):
    if  request.method == 'POST':
        entry_info = request.POST['entry_info']
        Entry.objects.create(entry_owner=request.user, entry_info=entry_info)
        #created_at is run in the background when create() is called
        return redirect('journal_entries')
    return render(request, 'journal/create_entry.html')
@login_required
def entry_detail(request, pk):
    entry_details = Entry.objects.get(pk=pk)
    return render(request, 'journal/entry_details.html', {'entry_details': entry_details})