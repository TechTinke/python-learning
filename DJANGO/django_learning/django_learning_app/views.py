from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #whatever is done to this function is what will be assigned to the URL
    # name = 'Erick'
    # # name = user.name

    # context = {
    #     'name': 'Erick',
    #     'age': 19,
    #     'nationality': 'British'
    # }
    return render(request, 'index.html')

def counter(request):
    input_text = request.GET['input_text']
    amount_of_words = len(input_text.split())
    return render(request, 'counter.html', {'amount_of_words': amount_of_words})
