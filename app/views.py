from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from .models import TemplateData,APIData,CreateContact,MessageTemplate,Webhook,Conversation

from .serializers import TempSerializer,ApiSerializer,MessageTemplateSerializer,CreateContactSerializer,WebhookSerializer,ConversationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from app import serializers



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

        serializer = ConversationSerializer(data = res)
        if serializer.is_valid():
            Conversation.objects.create(id=res['number']+"123",receiver_id = res['number'] , text = res)


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


    


class GetMsg(APIView):
    def get(self, request, format=None):


        response = requests.request("GET",url = '')

        if response.status_code == 200:

        
            data = response.json()

            Webhook.objects.create(ticketId=data['ticketId'],text=data['text'],eventType=data['eventType'],statusString=data['statusString'],waId = data['waId'])
            queryset = Webhook.objects.all()
            serializer = WebhookSerializer(queryset,many = True)
            filterset_fields = ['waId']

            response = {
                'status': True,
                'message': 'Data fetched successfully.',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        

        return Response("ERROR",status=status.HTTP_400_BAD_REQUEST)



class Conversation(APIView):
    pass
    # def post(self,request,format=None):
    #     if request.method == "POST":
    #         res = request.data

    #         serialize = ConversationSerializer(data=res)
    #         if serialize.is_valid():

    #             Conversation.objects.create(id=res['id'],res=data['text'],eventType=data['eventType'],statusString=data['statusString'],waId = data['waId'])

            

