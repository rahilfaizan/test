from django.db import models

class APIData(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
