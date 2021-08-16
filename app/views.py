from django.db.models import Q
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from .models import TemplateData,APIData,CreateContact,MessageTemplate,Webhook,Conversation
import json
from .serializers import TempSerializer,ApiSerializer,MessageTemplateSerializer,CreateContactSerializer,WebhookSerializer,ConversationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from app import serializers
from rest_framework.filters import SearchFilter



# orderOf = apitest.data
class ApiList(APIView):

    def get(self, request, format=None):

        cnumb = []
        cnam = []
        cstat = []
        data = {}

        url = "https://live-server-2553.wati.io/api/v1/getContacts"


        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MzE5NjQxMC1iNDA2LTQ0ZDktOWFiYy1lZTE5ZmZiZWMzNWEiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDgvMDMvMjAyMSAwNToyOToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.d8Z083VdTnmkv4k86NTY6oU6PhRhEi_ldUc-7cHN9Sg"}

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:


            data = response.json()

            for d in range(0, len(data["contact_list"])):
                contact_number = data["contact_list"][d]["wAid"]
                contact_name = data["contact_list"][d]["fullName"]
                contact_status = data["contact_list"][d]["contactStatus"]


                cnumb.append(contact_number)

                cnam.append(contact_name)

                cstat.append(contact_status)




            for i in range(0, len(data["contact_list"])):
                
                
                
                APIData.objects.update_or_create(number=cnumb[i],name=cnam[i],status=cstat[i])
            queryset = APIData.objects.all()
            serializer = ApiSerializer(queryset,many = True)
            # filterset_fields = ['number','name','status']

            response = {
                'status': True,
                'message': 'Data fetched successfully.',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        

        return Response("ERROR",status=status.HTTP_400_BAD_REQUEST)


# order = templatedata.data
class TempList(APIView):
    def get(self, request, format=None):
        id = []
        e_name = []
        cat = []
        body = []

        url = "https://live-server-2553.wati.io/api/v1/getMessageTemplates"


        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MzE5NjQxMC1iNDA2LTQ0ZDktOWFiYy1lZTE5ZmZiZWMzNWEiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDgvMDMvMjAyMSAwNToyOToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.d8Z083VdTnmkv4k86NTY6oU6PhRhEi_ldUc-7cHN9Sg"}

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:

        
            data = response.json()
            for d in range(0, len(data["messageTemplates"])):
                template_id = data["messageTemplates"][d]["id"]
                template_ename = data["messageTemplates"][d]["elementName"]
                template_cat = data["messageTemplates"][d]["category"]
                template_body = data["messageTemplates"][d]["body"]

                id.append(template_id)

                e_name.append(template_ename)

                cat.append(template_cat)
                body.append(template_body)



            for i in range(0, len(data["messageTemplates"])):
                        TemplateData.objects.update_or_create(id=id[i],element_name=e_name[i],category=cat[i],body=body[i])
            queryset = TemplateData.objects.all()
            serializer = TempSerializer(queryset,many = True)
            # filterset_fields = ['id','element_name','category','body']

            response = {
                'status': True,
                'message': 'Data fetched successfully.',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        

        return Response("ERROR",status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def PostMessage(request):
    if request.method == "POST":

        res = request.data
        serialize = MessageTemplateSerializer(data=res)
        if serialize.is_valid():

            MessageTemplate.objects.update_or_create(number = res['number'] , name = res['name'], val = res['val'] , broadcast_name = res['broadcast_name'], template_name = res['template_name'])

        url = "https://live-server-2553.wati.io/api/v1/sendTemplateMessage"
        payload = "{\"parameters\":[{\"name\":\""+res['name']+'\",\"value\":\"'+res['val']+"\"}],\"broadcast_name\":\""+res['broadcast_name']+"\",\"template_name\":\""+res['template_name']+"\"}"

        querystring = {"whatsappNumber":res['number']}

        headers = {
            "Content-Type": "application/json-patch+json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4ODkxY2IzOC0zYmMyLTQ4Y2QtYTg1Ni1kMzU1NWVhZWVjNDAiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDcvMzEvMjAyMSAwNTo0OToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.Rb0BUVwOjbQC1WDY4GxoZivv2Dk2NSnUFwXDKyaJn90"
        }
        r = requests.request('POST', url, data=payload, headers=headers , params=querystring)
        if r.status_code == 200:
            data = r.json()
            Conversation.objects.create(sender='us', receiver_id=res['number'], text=res['template_name'],number = res['number'])
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def PostContact(request):
    if request.method == "POST":
        res = request.data
        serialize = CreateContactSerializer(data=res)
        if serialize.is_valid():
            CreateContact.objects.update_or_create(number = res['number'] , name = res['name'], val = res['val'] , fullName = res['fullName'])
        if res['number'][:2] == "91" and len(res['number']==12):   
            url = "https://live-server-2553.wati.io/api/v1/addContact/"+res['number']

        elif res['number'][0] == "0" and len(res['number']==11):
            res["number"] = res["number"][1:]
            url = "https://live-server-2553.wati.io/api/v1/addContact/91"+res['number']


        else:
            url = "https://live-server-2553.wati.io/api/v1/addContact/91"+res['number']

        payload = "{\"customParams\":[{\"name\":\""+res['name']+'\",\"value\":\"'+res['val']+"\"}],\"name\":\""+res['fullName']+"\"}"


        headers = {
            "Content-Type": "application/json-patch+json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4ODkxY2IzOC0zYmMyLTQ4Y2QtYTg1Ni1kMzU1NWVhZWVjNDAiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDcvMzEvMjAyMSAwNTo0OToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.Rb0BUVwOjbQC1WDY4GxoZivv2Dk2NSnUFwXDKyaJn90"
        }
        r = requests.request('POST', url, data=payload, headers=headers)
        if r.status_code == 200:
            data = r.json()
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Request failed"}, status=r.status_code)

    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def first(request):
#     if request.method == "POST":
#         res = json.loads(request.body.decode("utf-8"))
#         serialize = MessageTemplateSerializer(data=res)
#         if serialize.is_valid():
#
#             MessageTemplate.objects.update_or_create(number = res['number'] , name = res['name'], val = res['val'] , broadcast_name = res['broadcast_name'], template_name = res['template_name'])
#
#         url = "https://live-server-2553.wati.io/api/v1/sendTemplateMessage"
#         payload = "{\"parameters\":[{\"name\":\""+res['name']+'\",\"value\":\"'+res['val']+"\"}],\"broadcast_name\":\""+res['broadcast_name']+"\",\"template_name\":\""+res['template_name']+"\"}"
#
#         querystring = {"whatsappNumber":res['number']}
#
#         headers = {
#             "Content-Type": "application/json-patch+json",
#             "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4ODkxY2IzOC0zYmMyLTQ4Y2QtYTg1Ni1kMzU1NWVhZWVjNDAiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDcvMzEvMjAyMSAwNTo0OToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.Rb0BUVwOjbQC1WDY4GxoZivv2Dk2NSnUFwXDKyaJn90"
#         }
#         r = requests.request('POST', url, data=payload, headers=headers , params=querystring)
#         if r.status_code == 200:
#             data = r.json()
#             Conversation.objects.create(sender='us', receiver_id=res['number'], text=res['template_name'],number = res['number'])
#             return Response(data, status=status.HTTP_200_OK)
#         return Response({"error": "Request failed"}, status=r.status_code)
#     else:
#          return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
#
#


@api_view(['POST'])
def GetMessage(request):
        if request.method == "POST":
            res = request.data
            serialize = WebhookSerializer(data=res)
            #Conversation.objects.create(id=res['number'], receiver_id=res['us'], text=res['text'])
            if serialize.is_valid():
                Webhook.objects.create(id=res['id'], receiver_id ='us', ticketId=res['ticketId'],
                                                         text=res['text'],
                                                         waId=res['waId'],conversationId=res['conversationId'])
                Conversation.objects.create(sender=res['waId'], receiver_id='us', text=res['text'],number  = res["waId"])

                if res['text'] == 'pay later':
                    serialize = MessageTemplateSerializer(data=res)
                    if serialize.is_valid():
                        MessageTemplate.objects.create(number=res['waId'], val=res['waId'],
                                                                 broadcast_name='thanking',
                                                                 template_name='thank_you_message')

                    url = "https://live-server-2553.wati.io/api/v1/sendTemplateMessage"
                    # payload = "{\"parameters\":[{\"name\":\""+res['ticketId']+'\",\"value\":\"'+res['waId']+"\"}],\"template_name\":\"thank_you_message\",\"broadcast_name\":\"thanking\"}"

                    payload = "{\"parameters\":[{\"name\":\"name\",\"value\":\""+res['waId']+"\"}],\"template_name\":\"thank_you_message\",\"broadcast_name\":\"test\"}"

                    querystring = {"whatsappNumber": res['waId']}
                    # [{\"name\":\""+res['name']+'\",\"value\":\"'+res['val']+"\"}]
                    #  "{\"parameters\":[{\"name\":\""+res['name']+'\",\"value\":\"'+res['val']+"\"}],\"broadcast_name\":\""+res['broadcast_name']+"\",\"template_name\":\""+res['template_name']+"\"}"

                    headers = {
                        "Content-Type": "application/json-patch+json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4ODkxY2IzOC0zYmMyLTQ4Y2QtYTg1Ni1kMzU1NWVhZWVjNDAiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDcvMzEvMjAyMSAwNTo0OToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.Rb0BUVwOjbQC1WDY4GxoZivv2Dk2NSnUFwXDKyaJn90"
                    }
                    r = requests.request('POST', url, data=payload, headers=headers, params=querystring)
                    if r.status_code == 200:
                        data = r.json()
                        Conversation.objects.create(sender='us', receiver_id=res['waId'], text='thank_you_message',
                                                    number=res['waId'])
                        return Response(data, status=status.HTTP_200_OK)
                    return Response({"error": "Request failed"}, status=r.status_code)
                else:
                    return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


            else:

                return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def Convo(request):
    number_entered_by_user = request.query_params.get('number')
    users = set()
    msgs = Conversation.objects.filter(Q(sender='us') | Q(receiver_id='us')).order_by('-sent')
    res = []
    for msg in msgs:
        if msg.sender == Conversation and msg.receiver_id.id not in users:
            users.add(msg.receiver_id.id)
            res.append(msg.id)
        elif msg.receiver_id == Conversation and msg.sender.id not in users:
            users.add(msg.sender.id)
            res.append(msg.id)
    if number_entered_by_user:
        queryset = Conversation.objects.filter(number=number_entered_by_user).order_by('-sent')
    else:
        queryset = Conversation.objects.all().order_by('-sent')

    serializer = ConversationSerializer(queryset, many=True)
    response = {
        'status': True,
        'message': 'Data fetched successfully.',
        'data': serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)