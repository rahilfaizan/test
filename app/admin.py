from django.contrib import admin
from .models import APIData,TemplateData,SenderData

admin.site.register(APIData)
class APIDataAdmin(admin.ModelAdmin):
    list_display = ['number','name','status']

admin.site.register(TemplateData)
class TemplateDataAdmin(admin.ModelAdmin):
    list_display = ['id','element_name','category','body']

admin.site.register(SenderData)
class SenderDataAdmin(admin.ModelAdmin):
    list_display = ['text','created','t_id']



