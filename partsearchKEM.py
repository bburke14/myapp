import http.client
import json
import csv


def partSearch(part_num):
    digikey_part_num = {
      "Part": part_num
    }
    encoded = json.dumps(digikey_part_num)

    conn.request("POST", "/services/partsearch/v2/partdetails", encoded, headers)
    res = conn.getresponse()
    data = res.read()

    result = json.loads(data)

    pd = result["PartDetails"]
    return pd

def findDetails(pd):
    tempList = []
    for item in pd["Parameters"]:
        tempList.append(item)
    return tempList

def readPartList():
    tempList = []
    with open('KEMpartlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, line in enumerate(reader):
            for key in line:
                tempList.append(line[key])
    return tempList

def writeToCSV(pd, writer, detailList):
    csvObj = {
              'ManufacturerName': pd["ManufacturerName"],
              'DKPartNumber': pd["DigiKeyPartNumber"],
              'ProductDescription': pd["ProductDescription"],
              'QuantityOnHand': pd["QuantityOnHand"],
              'AvailableOnOrder': str(pd["AvailableOnOrder"]),
              'ManfacturerPublicQuantity': pd["ManfacturerPublicQuantity"],
              'UnitPrice': pd["UnitPrice"],
              'ManufacturerLeadWeeks': pd["ManufacturerLeadWeeks"],
              'StandardPackage': pd["StandardPackage"],
              'MinimumOrderQuantity': pd["MinimumOrderQuantity"],
              'Url': "www.digikey.com"+pd["PartUrl"]
              }
    for i in detailList:
        csvObj[i["Parameter"]] = i["Value"]

    writer.writerow(csvObj)
#'UnitPrice': pd["UnitPrice"],'ManufacturerLeadWeeks': pd["ManufacturerLeadWeeks"],'StandardPackage': pd["StandardPackage"],'MinimumOrderQuantity': pd["MinimumOrderQuantity"],

part_num_list = readPartList()

token = "5KS5i0EDNQFPH3N6JrRdfBq8LkAr"

conn = http.client.HTTPSConnection("api.digikey.com")

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

with open('partsearchKEM.csv', 'w', newline='') as csvfile:
    fieldnames = ['ManufacturerName', 'DKPartNumber', 'ProductDescription', 'QuantityOnHand', 'AvailableOnOrder', 'ManfacturerPublicQuantity', 'UnitPrice', 'ManufacturerLeadWeeks', 'StandardPackage', 'MinimumOrderQuantity', 'Url', 'Packaging', 'Part Status', 'Capacitance', 'Tolerance', 'Voltage - Rated', 'Type', 'ESR (Equivalent Series Resistance)', 'Operating Temperature', 'Lifetime @ Temp.', 'Mounting Type', 'Package / Case', 'Size / Dimension', 'Height - Seated (Max)', 'Lead Spacing', 'Manufacturer Size Code', 'Features', 'Failure Rate', 'Notification', 'Applications', 'Temperature Coefficient', 'Thickness (Max)', 'Lead Style', 'Ratings']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for part in part_num_list:
        res = partSearch(part)
        detailList = findDetails(res)
        writeToCSV(res, writer, detailList)
        findDetails(res)

#'QuantityOnHand': pd["QuantityOnHand"],
