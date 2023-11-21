from app2.views import *
from django.urls import path

app_name='Bestfriend'
urlpatterns=[
    path('siva/',siva,name='siva'),
]