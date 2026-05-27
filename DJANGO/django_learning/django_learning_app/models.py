from django.db import models

# Create your models here.
# class Feature():
#     id: int
#     name: str
#     details: str
#     is_true: bool

#DATABASE CREATION
# The models created here are directly linked to the objects created in the Adminstrator Panel/Dashboard
class Feature(models.Model): #each object created using models.Model has an id.
    name = models.CharField(max_length=100) # a string of fields that collects characters
    details = models.CharField(max_length=500)