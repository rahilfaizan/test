import requests
import json


id = []
e_name = []
cat = []
body = []

url = "https://live-server-2553.wati.io/api/v1/getMessageTemplates"


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MzE5NjQxMC1iNDA2LTQ0ZDktOWFiYy1lZTE5ZmZiZWMzNWEiLCJ1bmlxdWVfbmFtZSI6IlNvbmFtQGtzbGVnYWwuY28uaW4iLCJuYW1laWQiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiZW1haWwiOiJTb25hbUBrc2xlZ2FsLmNvLmluIiwiYXV0aF90aW1lIjoiMDgvMDMvMjAyMSAwNToyOToxNCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFETUlOSVNUUkFUT1IiLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoiQ2xhcmVfQUkiLCJhdWQiOiJDbGFyZV9BSSJ9.d8Z083VdTnmkv4k86NTY6oU6PhRhEi_ldUc-7cHN9Sg"}

response = requests.request("GET", url, headers=headers)


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

