from django.db import models

class Blog(models.Model):
    """Blog model"""
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="Blog_images/")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %B %Y')
