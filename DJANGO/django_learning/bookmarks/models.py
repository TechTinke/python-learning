from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Link(models.Model):
    link_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=250)
    details = models.CharField(max_length=300)