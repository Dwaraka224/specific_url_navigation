from app1.views import *
from django.urls import path
app_name='friend'
urlpatterns=[
    path('dwaraka/',dwaraka,name='dwaraka'),
]