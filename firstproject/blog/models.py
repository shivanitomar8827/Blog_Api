from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    
    sort_description = models.CharField(max_length=500)










