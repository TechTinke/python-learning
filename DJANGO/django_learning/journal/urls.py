from . import views
from django.urls import path
urlpatterns = [
    path('', views.login, name='login'),
    path('journal_entries', views.journal_entries, name='journal_entries'),
    path('create_entry', views.create_entry, name='create_entry'),
    path('entry/<str:pk>', views.entry_detail, name='entry_detail')
]