from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset
import pandas as pd
import json
import os

# Create API to add dataset form the user
@api_view(['POST'])
def upload_data(request):
    try:
        # Gather all the data for the user
        data = json.loads(request.body)
        
        # Check the data
        if not data:
            return Response({'result': False, 'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Extract the data sent from the frontend
        name = data.get('name'),
        data_type = data.get('data_type')
        df = data.get('df')
        user = data.get('user')

        os.makedirs('./base_data', exist_ok=True)
        os.makedirs('./modified_data', exist_ok=True)
        df.to_csv(f'./base_data/{name}.csv', index=False)
        df.to_csv(f'./modified_data/{name}.csv', index=False)
        
        try:
            # create a dataset entry into the database
            dataset = Dataset(
                name = name,
                data_type = data_type,
                base_path = f'./base_data/{name}.csv',
                modified_path = f'./modified_data/{name}.csv',
                user = user,
            )
            dataset.save()
            
            return Response({'result': True, 'message': 'Dataset is created successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

# API to get data details to display on page
@api_view(['GET'])
def get_datasets(requests, pk):
    try:
        if Dataset.objects.filter(user=pk).exists():
            # Get data based on the user ID
            datasets = Dataset.objects.filter(user=pk).all()

            # Extract the data and send it to the frontend
            res = []
            for data in datasets:
                dataset = {
                    'name': data.name,
                    'id' : data.pk
                }
                res.append(dataset)
            return Response({'result': True, 'datasets': res}, status=status.HTTP_200_OK)
        else:
            return Response({'result': True, 'datasets': {}}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
# Load data for the front end
@api_view(['GET'])
def load_data(request, pk):
    try:
        # Get data requested by the user
        if Dataset.objects.filter(pk=pk).exists():
            temp = Dataset.objects.filter(pk=pk).first()
            base_df = pd.read_csv(temp.base_path)
            modified_df = pd.read_csv(temp.modified_path)

            res = {
                'base df': base_df,
                'modified_df': modified_df
            }
            return Response({'result': True, 'datasets': res}, status=status.HTTP_200_OK)
        else:
            return Response({'result': False, 'error': "unable to fetch the data from the database"}, status=status.HTTP_400_BAD_REQUEST)  
    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def save_data(request):
    try:
        # Gather all the data for the user
        data = json.loads(request.body)
        
        # Check the data
        if not data:
            return Response({'result': False, 'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        df = data.get('modified_df')
        name = data.get('name')
        df.to_csv(f'./modified_data/{name}.csv', index=False)

        return Response({'result': True, 'message': "File saved successfully in the database."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'result': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)
    
########################################################
#  All the Dataset functions(basic) are done for now.  #
########################################################
