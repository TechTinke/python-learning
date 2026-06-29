from django.shortcuts import render, redirect #redirect - allows us to redirect the user to another page once they have signed up  
from django.http import HttpResponse
from django.contrib.auth.models import User, auth # User - User model in the Django Administration Panel , auth - functions used to authenticate
from django.contrib import messages
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

    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.details = 'Our service is very reliable' 

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Secure'
    # feature3.details = 'Our service is very secure'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Easy to use'
    # feature4.details = 'Our service is easy to use'

    # # return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2})

    # features = [feature1, feature2, feature3, feature4] # Dynamic way of doing it instead each at a time

    features = Feature.objects.all() #gets all the objects created from Feature and stores them in the variable features
    return render(request, 'django_learning_app/index.html', {'features':features})
#this is then passed in the template files e.g
#<h4 class='title'><a href=''>{{feature1.name}}</a></h4>
#<p class='description'>{{feature1.details}}</p>

# <!-- USING LOOPS IN HTML -->
# <!-- {% for feature in features %} -->
# <!-- {% if feature.is_true == True %} -->
# <!-- <p>This feature is true</p> -->
# <!-- {{% else %}} -->
# <!-- <p>This feature is False</p> -->
# <!-- {{% endif %}} -->
# <!-- {{% endfor %}} -->

# NB: SINCE 
# def counter(request):
#     input_text = request.POST['input_text']
#     # input_text = request.POST.get('input_text', '') #Using .get() instead of [] prevents the MultiValueDictKeyError even if the key is missing for some reason.
#     amount_of_words = len(input_text.split())
#     return render(request, 'counter.html', {'amount_of_words': amount_of_words})

# NB:
# - request.user is never empty(None) when no one is logged in.
# - A special placeholder(AnonymousUser) is used when no one is authenticated
# - Anonymous user returns False when user.is_authenticated is run so that there is no crash
def register(request):
    if request.method == 'POST': #if this page is being rendered using the POST method, sth is being send to the 'register' view; which is the data below
        username = request.POST['username'] #data collected from username is stored inside this variable
        email = request.POST['email'] #email
        password = request.POST['password'] #password
        password2 = request.POST['password2'] #password2

        if password == password2:
            if User.objects.filter(email=email).exists(): #checking if there exists an email from the Django User Administration Panel from the one that the user created using the Sign Up form
                messages.info(request, "Email already used") #message send to the user if the email already exists
                return redirect('register') #User is redirected back to register because the email already exists
            elif User.objects.filter(username=username).exists(): #checking if there exists an username from the Django User Administration Panel from the one that the user created using the Sign Up form
                messages.info(request, "That username already exists") #message send to the user if the username already exists
                return redirect('register') #User is redirected back to register because the username already exists
            else:
                user = User.objects.create_user(username=username, email=email, password=password) #creating the user with the credentials used 
                user.save(); #Saving the user that was created
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'django_learning_app/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password) #authenticating user details from credentials on Django Panel(username, password)
        if user is not None: #user is registered
            auth.login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'Oops, your login credentials could not be found!')
            return redirect('login')
    else:
        return render(request, 'django_learning_app/login.html')

def welcome(request):
    return render(request, 'django_learning_app/welcome.html')

def logout(request):
    auth.logout(request)
    return redirect('/django_learning_app/')

def post(request, pk):
    return render(request, 'django_learning_app/post.html', {'pk': pk})

def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'django_learning_app/counter.html', {'posts': posts})


