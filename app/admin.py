from django.contrib import admin
from .models import APIData

admin.site.register(APIData)
class APIDataAdmin(admin.ModelAdmin):
    list_display = ['number','name','status']

