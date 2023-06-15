from django.db import models







class blog(models.Model):
    title = models.CharField(max_length=500)
    descr = models.CharField(max_length=500)
    image = models.ImageField()
    sort_descr = models.CharField(max_length=500)



