from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    writer=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]