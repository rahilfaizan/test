from django.shortcuts import render
import requests
from .models import APIData
from .import apitest
from .serializers import ApiSerializer

from rest_framework.generics import ListAPIView



def index(request):
    cnumb = apitest.cnumb
    cname = apitest.cnam
    cstatus = apitest.cstat

    # print(cnumb,cname,cstatus)

    for i in range(0,2):
        value = APIData(
            
            number = cnumb[i],
            name = cname[i],
            status = cstatus[i]
        )
        value.save()
    data = APIData.objects.all()

    return render(request,'base.html',{'data':data})

class ApiList(ListAPIView):
    queryset = APIData.objects.all()
    serializer_class = ApiSerializer
    filterset_fields = ['number','name','status']
    