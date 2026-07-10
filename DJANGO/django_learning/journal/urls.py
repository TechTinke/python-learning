from . import views
from django.urls import path
urlpatterns = [
    path('', views.login, name='login'),
    path('/journal_entires', views.journal_entries, name='journal_entries'),
    path('entry/<str:pk>', views.entry_details, name='entry_details')
]