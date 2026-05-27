from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request): #whatever is done to this function is what will be assigned to the URL
    # name = 'Erick'
    # # name = user.name

    # context = {
    #     'name': 'Erick',
    #     'age': 19,
    #     'nationality': 'British'
    # }
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is very reliable' 

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Secure'
    feature3.details = 'Our service is very secure'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Easy to use'
    feature4.details = 'Our service is easy to use'

    # return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2})

    features = [feature1, feature2, feature3, feature4] # Dynamic way of doing it instead each at a time
    return render(request, 'index.html', {'features':features})
  
#this is then passed in the template files e.g
#<h4 class='title'><a href=''>{{feature1.name}}</a></h4>
#<p class='description'>{{feature1.details}}</p>

def counter(request):
    input_text = request.POST['input_text']
    # input_text = request.POST.get('input_text', '') #Using .get() instead of [] prevents the MultiValueDictKeyError even if the key is missing for some reason.
    amount_of_words = len(input_text.split())
    return render(request, 'counter.html', {'amount_of_words': amount_of_words})
