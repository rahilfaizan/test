from rest_framework import serializers
from .models import APIData,TemplateData,MessageTemplate,CreateContact, Webhook,Conversation

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIData
        fields = ['number','name','status']

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateData
        fields = ['id','element_name','category','body']


class MessageTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTemplate
        fields = "__all__"

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContact
        fields = "__all__"


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = "__all__"

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = "__all__"

      