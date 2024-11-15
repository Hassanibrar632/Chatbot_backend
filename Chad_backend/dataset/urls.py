from django.urls import path
from .views import *

urlpatterns = [
    path('/upload', upload_data, name='upload'),
    path('/get/<int:pk>', get_datasets, name='list'),
    path('/load/<int:pk>', load_data, name='load'),
    path('/save', save_data, name='save'),
]