from django.db import models

class APIData(models.Model):
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class TemplateData(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    element_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    body = models.TextField(max_length=200)

class SenderData(models.Model):
    text = models.TextField(max_length=200)
    created = models.CharField(max_length=50)
    t_id = models.TextField()
    

