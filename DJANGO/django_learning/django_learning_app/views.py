from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #whatever is done to this function is what will be assigned to the URL
    return render(request, 'index.html')
