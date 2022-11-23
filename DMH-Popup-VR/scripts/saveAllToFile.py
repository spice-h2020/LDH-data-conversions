import requests
from requests.auth import HTTPBasicAuth
import json

# replace <dataset-id> with the id of your LDH dataset (eg 1e08cf4f-9607-411d-93bd-ee18c019fea9 )
# replace <access-key> with the LDH API key that has write permission to push docs into your dataset
baseUrl = 'https://api2.mksmart.org/object/'
dataset = '<dataset-id>'
datasetKey = '<access-key>'
limit = 5000

headers = {
        'Content-Type': 'application/json'
    }

fullUrl = baseUrl + dataset + '?limit=' + str(limit)
response = requests.request("GET", fullUrl, headers=headers, auth=HTTPBasicAuth(datasetKey, datasetKey))
# responseText is the raw JSON straight from the API
responseText = response.text
# responseObject is a Python readable object, should you wish to iterate over the data and manipulate it in any way
# also, we'll re-encode this object back to JSON for saving so that we can format the text with indentation
responseObject = response.json()
# e.g. if you'd like to print the 'name' attribute of the first document in the array:
print(responseObject[0]['name'])

# write new object out to a new JSON file
outputFilename = '../output/' + dataset + '.json'
with open(outputFilename, 'w', encoding='utf-8') as f:
    json.dump(responseObject, f, ensure_ascii=False, indent=4)
