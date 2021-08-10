from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from .models import TemplateData,SenderData,APIData,CreateContact,MessageTemplate
from .import apitest,templatedata,getmessage
from .serializers import TempSerializer,MsgSerializer,ApiSerializer,MessageTemplateSerializer,CreateContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from rest_framework.generics import ListAPIView

from app import serializers

cnumb = apitest.cnumb
cname = apitest.cnam
cstatus = apitest.cstat

id = templatedata.id
e_name = templatedata.e_name
cat = templatedata.cat
body = templatedata.body

text1 = getmessage.text
created1 = getmessage.created
t_id1 = getmessage.ticket_id


orderOf = apitest.data
class ApiList(ListAPIView):
    for i in range(0, len(orderOf["contact_list"])):
        
        
        # x.append(APIData(number=cnumb[i], name=cname[i], status=cstatus[i]))
        # if i % 100 == 0:
        APIData.objects.update_or_create(number=cnumb[i],name=cname[i],status=cstatus[i])
    queryset = APIData.objects.all()
    serializer_class = ApiSerializer
    filterset_fields = ['number','name','status']


order = templatedata.data
class TempList(ListAPIView):
    for i in range(0, len(order["messageTemplates"])):
                TemplateData.objects.update_or_create(id=id[i],element_name=e_name[i],category=cat[i],body=body[i])
    queryset = TemplateData.objects.all()
    serializer_class = TempSerializer
    filterset_fields = ['id','element_name','category','body']

orderm = []
for i in range(0,11):
    orderm.append(getmessage.data)
class SndList(ListAPIView):
        for i in range(0, 11):
                    SenderData.objects.update_or_create(text = text1[i] , created = created1[i] ,t_id = t_id1[i])
        queryset = SenderData.objects.all()
        serializer_class = MsgSerializer
        filterset_fields = ['text','created','t_id']


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
            
        url = "https://live-server-2553.wati.io/api/v1/addContact/"+res['number']
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


    


