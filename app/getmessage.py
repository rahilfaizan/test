import requests
import json
from .models import APIData


text = []
created = []
ticket_id = []


apidata = APIData.objects.values_list('number')

for i in range(0,len(apidata)):
    numb = apidata[i]
    numb = numb[0]
    


    url = "https://live-server-2553.wati.io/api/v1/getMessages/{num}".format(num=numb)

    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MzE5NjQxMC1iNDA2LTQ0ZDktOWFiYy1lZTE5ZmZiZWMzNWEiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDgvMDMvMjAyMSAwNToyOToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.d8Z083VdTnmkv4k86NTY6oU6PhRhEi_ldUc-7cHN9Sg"}

    response = requests.request("GET", url, headers=headers)

    tocheck = response.json()

    if tocheck['result'] == 'success': 
        data = response.json()

    

        for d in range(0,len(data['messages']['items'])):

            if len(data['messages']['items'][d])==19 :
                tex = data['messages']['items'][d]['text']
                cre = data['messages']['items'][d]['created']
                tick = data['messages']['items'][d]['ticketId']

                text.append(tex)
                created.append(cre)
                ticket_id.append(tick)
