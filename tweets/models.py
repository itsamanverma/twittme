from django.db import models

# Create your models here.

class Tweet(models.Model):
    # id = models.AutoFeild(primary_key=True)
    content = models.TextField(max_length=200)
    image   = models.FileField(upload_to='images/', blank=True, null=True)