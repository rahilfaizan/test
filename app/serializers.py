from rest_framework import serializers
from .models import APIData,TemplateData,SenderData,MessageTemplate,CreateContact

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIData
        fields = ['number','name','status']

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateData
        fields = ['id','element_name','category','body']

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderData
        fields = ['text','created','t_id']

class MessageTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTemplate
        fields = "__all__"

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContact
        fields = "__all__"

      