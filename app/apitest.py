import requests
import json
# from .models import APIData

cnumb = []
cnam = []
cstat = []
data = {}

url = "https://live-server-2553.wati.io/api/v1/getContacts"


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MzE5NjQxMC1iNDA2LTQ0ZDktOWFiYy1lZTE5ZmZiZWMzNWEiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDgvMDMvMjAyMSAwNToyOToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.d8Z083VdTnmkv4k86NTY6oU6PhRhEi_ldUc-7cHN9Sg"}

response = requests.request("GET", url, headers=headers)

data = response.json()

for d in range(0, len(data["contact_list"])):
    contact_number = data["contact_list"][d]["wAid"]
    contact_name = data["contact_list"][d]["fullName"]
    contact_status = data["contact_list"][d]["contactStatus"]
    # print(contact_number,end=' ')
    # print(contact_name,end=' ')
    # print(contact_status)

    cnumb.append(contact_number)

    cnam.append(contact_name)
        #print(cnam)
    #if contact_status not in cstat:
    cstat.append(contact_status)

# print(cnumb)
# print(cnam)
# print(cstat)



