from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    entry_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_info = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)