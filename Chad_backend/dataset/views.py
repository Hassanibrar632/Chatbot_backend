from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset
import json

# Create API to add dataset for the user
@api_view(['POST'])
def get_data(request):
    try:
        # Gather all the data for the user
        data = json.loads(request.body)
        # user = data.get('user')
        
        # Check the data
        if not data:
            return Response({'result': False, 'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if same dataset exsists
        if Dataset.objects.filter().exists():
            return Response({'result': False, 'error': 'User Already exits with the same email'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # create a dataset into the database
            
            return Response({'result': True, 'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

# API to get data details to display on page
@api_view(['GET'])
def get_datasets(requests, pk):
    try:
        # Get data based on the user ID
        data = Dataset.objects.filter(user=pk).all()

        # Extract the data from the user object
        
        
        return Response({'result': True, 'user': data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
# API to login into the account
@api_view(['POST'])
def load_data(request):
    try:
        # Gather all the data form the user's request 
        data = json.loads(request.body)
        pk = data
        # Get data based on username else with email
        if Dataset.objects.filter(pk=pk).exists():
            temp = Dataset.objects.filter(pk=pk).first()
        else:
            return Response({'result': False, 'error': "User or email doesn't exist in the datbase"}, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
########################################################
#  All the Dataset functions(basic) are done for now.  #
########################################################
