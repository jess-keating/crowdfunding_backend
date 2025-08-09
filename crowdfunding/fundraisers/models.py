from django.db import models

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_create = models.DateTimeField(auto_now_add=True)
    

# Create your models here.
