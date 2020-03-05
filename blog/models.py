from django.db import models

class Blog(models.Model):
    """Blog model"""
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="Blog_images/")
