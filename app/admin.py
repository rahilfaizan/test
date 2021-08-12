from django.contrib import admin
from .models import TemplateData,APIData,MessageTemplate,CreateContact

admin.site.register(APIData)
class APIDataAdmin(admin.ModelAdmin):
    list_display = ['number','name','status']

admin.site.register(TemplateData)
class TemplateDataAdmin(admin.ModelAdmin):
    list_display = ['id','element_name','category','body']


admin.site.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'val', 'broadcast_name','template_name']

admin.site.register(CreateContact)
class CreateContactAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'val', 'fullName']



