from django.urls import path
from .views import *

urlpatterns = [
    path("create", register_user, name='register_user'),
    path('auth', aunthicate_user, name='aunthicate_user'),
    path('get/<int:pk>', get_details, name='get_data'),
]