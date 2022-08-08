import requests
from requests.auth import HTTPBasicAuth
import json

# replace <dataset-id> with the id of your LDH dataset (eg f3883602-b187-47b1-9815-75ea7d12fbc5 )
# replace <access-key> with the LDH API key that has write permission to push docs into your dataset
url = "https://api2.mksmart.org/object/<dataset-id>"
LDHAccessKey = '<access-key>'
headers = {
        'Content-Type': 'application/json'
    }

# load JSON
with open('../output/individual_docs.json', encoding='utf-8') as f:
    inputData = json.load(f)

# For each JSON doc, push/upload it to the LDH API
for item in inputData:
    singleJsonDoc = json.dumps(item, ensure_ascii=True)
    response = requests.request("POST", url, headers=headers, auth=HTTPBasicAuth(LDHAccessKey, LDHAccessKey), data=singleJsonDoc)
    print(response.text)

