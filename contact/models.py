from django.db import models

# Create your models here.

class contact_model(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    message = models.TextField()