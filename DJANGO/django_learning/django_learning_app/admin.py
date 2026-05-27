from django.contrib import admin
from .models import Feature

# Register your models here.
admin.site.register(Feature)
# You need to import the models created and register them here in order to view them from the Django admin panel/dashboard