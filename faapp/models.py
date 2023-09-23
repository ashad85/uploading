from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class uplod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.CharField(max_length=300)
    Imag = models.ImageField(upload_to='media')
    docment = models.FileField(upload_to='media')