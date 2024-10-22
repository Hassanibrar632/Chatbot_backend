from django.urls import path, include
from .views import *

urlpatterns = [
    path('/temp', index, name='temp')
]