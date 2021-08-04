from rest_framework import serializers
from .models import APIData

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIData
        fields = ['number','name','status']