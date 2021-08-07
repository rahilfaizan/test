from rest_framework import serializers
from .models import APIData,TemplateData,SenderData

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

      