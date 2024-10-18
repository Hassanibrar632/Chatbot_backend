from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    User = models.CharField(max_length=25, unique=True)
    First_Name = models.CharField(max_length=25, blank=True)
    Last_Name = models.CharField(max_length=25, blank=True)
    Password = models.CharField(max_length=128)
    Created_date = models.DateField(auto_now_add=True)

    """
    So we have created a user datatable to save the data of user
    We have these columns:
    (ID auto created)
    1. email
    2. username
    3. First and Last name
    4. password
    5. user created date
    """
