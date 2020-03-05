from django.db import models

class Job(models.Model):
    """My jobs"""
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
