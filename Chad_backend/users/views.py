from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

@api_view(['GET'])
# Create API to add user for the chadbot
def register_user(request):
        # perform aunthication
        return Response({'Register': 'True or False', 'error': 'error'})

# Create API for Loginng in to the chadbot

