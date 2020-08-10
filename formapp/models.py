from django.db import models

# Create your models here.

class FormData(models.Model):
    name = models.CharField(max_length=264)
    email = models.CharField(max_length = 264, unique=True, default='default@default.com')
    college = models.CharField(max_length=264)