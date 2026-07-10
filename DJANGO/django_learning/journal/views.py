from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    pass
@login_required
def journal_entries(request):
    pass
@login_required
def entry_details(request, pk):
    pass