import http.client
import json


token = "R4xSI35nV4pPoRC45N8bc9iUeIwN"

conn = http.client.HTTPSConnection("api.digikey.com")

obj = {
  "SearchOptions": [
    "ChipOutpostOnly"
  ],
  "Keywords": "478-8910-2-ND",
  "RecordCount": "10",
  "RecordStartPosition": "0",

  "Sort": {
    "Option": "SortByManufacturerPartNumber",
    "Direction": "Ascending",
    "SortParameterId": 13750284
  },
  "RequestedQuantity": 26
}

# headers = {
#     'X-IBM-Client-Id': "c32a6a44-8532-4649-a426-ecd4b5ae7e54",
#     'content-type': "application/json",
#     'accept': "application/json",
#     'X-DIGIKEY-Locale-Site': "US",
#     'X-DIGIKEY-Locale-Language': "en",
#     'X-DIGIKEY-Locale-Currency': "USD",
#     'X-DIGIKEY-Locale-Shiptocountry': "",
#     'Authorization': "vOBzL2wJ0m32qVaP7fpXxdLR0grq"
#     }

headers = {
    'x-ibm-client-id': "c32a6a44-8532-4649-a426-ecd4b5ae7e54",
    'content-type': "application/json",
    'accept': "application/json",
    'x-digikey-locale-site': "US",
    'x-digikey-locale-language': "en",
    'x-digikey-locale-currency': "USD",
    'x-digikey-locale-shiptocountry': "",
    'x-digikey-customer-id': "",
    'x-digikey-partner-id': "",
    'authorization': token
    }

pay = json.dumps(obj)


conn.request("POST", "/services/partsearch/v2/keywordsearch", pay, headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
