from django.contrib import admin
from .models import TemplateData,APIData,MessageTemplate,CreateContact,Webhook,Conversation

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


admin.site.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ['id', 'receiver_id', 'ticketId', 'text','eventType','statusString','waId','conversationId']

admin.site.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'receiver_id','text','sent']



