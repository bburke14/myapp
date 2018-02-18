import http.client
import json
import csv

token = "R4xSI35nV4pPoRC45N8bc9iUeIwN"

conn = http.client.HTTPSConnection("api.digikey.com")

payload = "{\"Part\":\"arti\"}"

digikey_part_num = {
  "Part": "478-8630-2-ND"
}
encoded = json.dumps(digikey_part_num)


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

conn.request("POST", "/services/partsearch/v2/partdetails", encoded, headers)

res = conn.getresponse()
data = res.read()

result = json.loads(data)

#print(result["PartDetails"])
pd = result["PartDetails"]
#print(result["PartDetails"]["PartUrl"])
# print("Url:", pd["PartUrl"])
# print("DigiKey Part Numer:", pd["DigiKeyPartNumber"])
# print("Manufacturer Lead Weeks:", pd["ManufacturerLeadWeeks"])
# print("Manufacturer Public Quantity:", pd["ManfacturerPublicQuantity"])
# print("Available On Order:", pd["AvailableOnOrder"])

file = open("partsearchdump.txt", "w")
file.write("AvailableOnOrder: " + str(pd["AvailableOnOrder"]))

# with open("partsearchdump2.csv", "w", newline="") as csvfile:
#     fuck = csv.writer(csvfile, delimiter=" ",
#                       quotechar = '|', quoting=csv.QUOTE_MINIMAL)
#     fuck.writeheader()
#     fuck.writerow({"AvailOnOrder": str(pd["AvailableOnOrder"])})
#     fuck.writerow("AvailableOnOrder" + str(pd["AvailableOnOrder"]))

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['ManufacturerName', 'DKPartNumber', 'QuantityOnHand', 'AvailableOnOrder', 'Url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'ManufacturerName': pd["ManufacturerName"], 'DKPartNumber': pd["DigiKeyPartNumber"], 'QuantityOnHand': pd["QuantityOnHand"], 'AvailableOnOrder': str(pd["AvailableOnOrder"]), 'Url': "www.digikey.com"+pd["PartUrl"]})
#'QuantityOnHand': pd["QuantityOnHand"],
