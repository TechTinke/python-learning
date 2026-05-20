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
    input_text = request.POST['input_text']
    # input_text = request.POST.get('input_text', '') #Using .get() instead of [] prevents the MultiValueDictKeyError even if the key is missing for some reason.
    amount_of_words = len(input_text.split())
    return render(request, 'counter.html', {'amount_of_words': amount_of_words})
