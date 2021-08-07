from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from .models import APIData,TemplateData,SenderData
from .import apitest,templatedata,getmessage
from .serializers import ApiSerializer,TempSerializer,MsgSerializer

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

    # print(orderm)

# apidata = APIData.objects.values_list('number')

# for i in range(0,len(apidata)):
#     numb = apidata[i][0]
#     print(numb)

# print(orderm)


    


