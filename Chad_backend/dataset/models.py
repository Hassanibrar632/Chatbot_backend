from django.db import models

# Create your models here.

class Dataset(models.Model):
    name = models.CharField(max_length=25, unique=True)
    data_type = models.BooleanField()
    base_path = models.CharField(max_length=50)
    modified_path = models.CharField(max_length=50, null=True)
    user = models.PositiveIntegerField()
    Created_date = models.DateTimeField(auto_now_add=True)

    """
    So we have created a Dataset table to save the rescords of datafiles unloaded by the users
    We have these columns:
    (ID auto created)
    1. name(of the dataset)
    2. data_type(catagorical or regssive)
    3. base_path(untouched base file of the dataset)
    4. modified_path()
    5. user [ID](created the dataset)
    6. created date
    """
