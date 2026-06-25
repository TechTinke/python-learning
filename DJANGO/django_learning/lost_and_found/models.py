from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# NB:
# - Every field that is created with no null=True is a required field (non-nullable)

# - In cases when a new field has been created and that field is non-nullable 
# and the other fields have already been populated, an error is thrown and you
# have to set a default value from the terminal or set the default value manually from the model creation

# - A user who is not logged in is specially assigned as Anonymous User by Django
# but user.is_authenticated returns False when run
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # every Post row must have a real owner value
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)