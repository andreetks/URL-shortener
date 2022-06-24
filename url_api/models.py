from django.db import models

# Create your models here.

class Url(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=8, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
