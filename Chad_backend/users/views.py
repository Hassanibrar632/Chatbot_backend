from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import User
import json

# Create API to add user for the chadbot
@api_view(['POST'])
def register_user(request):
    try:
        # Gather all the data for the user
        data = json.loads(request.body)
        email = data.get('email')
        user = data.get('user')
        FName = data.get('FName')
        LName = data.get('LName')
        Pass = data.get('Pass')

        # Check the data
        if not user or not email or not Pass:
            return Response({'result': False, 'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if users exsists or not with the same username or email
        if User.objects.filter(email = email).exists():
            return Response({'result': False, 'error': 'User Already exits with the same email'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(User = user).exists():
            return Response({'result': False, 'error': 'User Already exits with the same username'}, status=status.HTTP_400_BAD_REQUEST)

        # encypt the password for saving
        Pass = make_password(Pass)

        try:
            # create a user into the database
            user = User(
                email = email,
                User = user,
                First_Name = FName,
                Last_Name = LName,
                Password = Pass
            )
            user.save()

            return Response({'result': True, 'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
# API to get users details to display on the profile page
@api_view(['GET'])
def get_details(requests, pk):
    try:
        # Get a user based on the value of the primary key
        user = User.objects.filter(pk=pk).first()

        # Extract the data from the user object
        user_data = {
            'email': user.email,
            'user': user.User,
            'first_name': user.First_Name,
            'last_name': user.Last_Name
        }
        
        return Response({'result': True, 'user': user_data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
# API to login into the account
@api_view(['POST'])
def aunthicate_user(request):
    try:
        # Gather all the data form the user's request 
        data = json.loads(request.body)
        user = data.get('user')
        Pass = data.get('Pass')
        
        # Get data based on username else with email
        if User.objects.filter(User=user).exists():
            temp = User.objects.filter(User=user).first()
        elif User.objects.filter(email=user).exists():
            temp = User.objects.filter(email=user).first()
        else:
            return Response({'result': False, 'error': "User or email doesn't exist in the datbase"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Extract the data based on the password match and return the data
        if check_password(Pass, temp.Password):
            print('match')
            return Response({'result': True, 'user': temp.pk}, status=status.HTTP_200_OK)
        else:
            print('nomatch')
            return Response({'result': False, 'error': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
######################################################
#  All the users functions(basic) are done for now.  #
######################################################
