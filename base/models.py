from django.db import models
from django.core.validators import MinLengthValidator
class User(models.Model):
    name = models.CharField(max_length=100,validators=[MinLengthValidator(1)])
    password  = models.CharField(max_length=100,validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    # Add any additional fields you need for your model

    def __str__(self):
        return self.file.name