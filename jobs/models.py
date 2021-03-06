from django.db import models

class Job(models.Model):
    """My jobs"""
    image = models.ImageField(upload_to='Job_images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
