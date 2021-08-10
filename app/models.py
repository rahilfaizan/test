from django.db import models

class APIData(models.Model):
    number = models.CharField(max_length=50,null = True,blank = True)
    name = models.CharField(max_length=50,null = True,blank = True)
    status = models.CharField(max_length=50,null = True,blank = True)

class TemplateData(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    element_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    body = models.TextField(max_length=200)

class SenderData(models.Model):
    text = models.TextField(max_length=200)
    created = models.CharField(max_length=50)
    t_id = models.TextField()

class MessageTemplate(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    val = models.CharField(max_length=20)
    broadcast_name = models.CharField(max_length=20)
    template_name = models.CharField(max_length=20)

class CreateContact(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    val = models.CharField(max_length=20)
    fullName = models.CharField(max_length=20)
    




    

