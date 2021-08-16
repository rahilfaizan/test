from datetime import datetime
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


class MessageTemplate(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    receiver_id = models.CharField(max_length=50,null=True,blank=True)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    val = models.CharField(max_length=20)
    broadcast_name = models.CharField(max_length=20)
    template_name = models.CharField(max_length=20)
    sent = models.DateTimeField(default=datetime.now, blank=True)

class CreateContact(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    val = models.CharField(max_length=20)
    fullName = models.CharField(max_length=20)
    
    

class Webhook(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    receiver_id = models.CharField(max_length=50,null=True,blank=True)
    ticketId = models.CharField(max_length=255)
    text = models.TextField()
    eventType = models.CharField(max_length=255)
    statusString = models.CharField(max_length=255)
    waId = models.CharField(max_length=255)
    conversationId = models.CharField(max_length=255,null=True,blank=True)
    sent = models.DateTimeField(default=datetime.now, blank=True)


class Conversation(models.Model):
    sender = models.CharField(max_length=50,null=True,blank=True)
    receiver_id = models.CharField(max_length=50,null=True,blank=True)
    conversationId = models.CharField(max_length=255,null=True,blank=True)
    text = models.TextField()
    number = models.CharField(max_length=255)
    sent = models.DateTimeField(default=datetime.now, blank=True)