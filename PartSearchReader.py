from bs4 import BeautifulSoup
import requests
import csv
import re
import http.client
import json

class PartSearchReader:
    def __init__(self, h):
        self.__headers = h

    def readUrlListFromCSV(self, fileName):
        templist = []
        with open(fileName, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, line in enumerate(reader):
                for key in line:
                    templist.append(line[key])
        return templist

    def getSoupData(self, url):
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def scrapeTopHalf(self, soup, dic):
        content = soup.find('div', attrs={'id': 'pdp_content'})
        tophalf = content.find('div', attrs={'id': 'tophalf'})
        productdetails1 = tophalf.find('table', attrs={'id': 'product-details'})
        list_of_headers = []
        list_of_cells = []

        for row in productdetails1.find_all('tr'):
            for header in row.find_all('th'):
                header_content = header.get_text()
                clean_headers = re.sub( '\r\n', ' ', header_content).strip()
                clean_headers2 = re.sub( '\n\n', ' ', clean_headers).strip()
                list_of_headers.append(clean_headers2)

            for value in row.find_all('td'):
                value_content = value.get_text()
                clean_values = re.sub( '\r\n', ' ', value_content).strip()
                clean_values2 = re.sub( '\n\n', ' ', clean_values).strip()
                list_of_cells.append(clean_values2)

        counter = 0
        for h in list_of_headers:
            dic[h] = list_of_cells[counter]
            counter = counter + 1

        return dic

    def scrapeRightCol(self, soup, dic):
        content = soup.find('div', attrs={'id': 'pdp_content'})
        right_col = content.find('div', attrs={'id': 'rightcolumn'})
        product_dollars = right_col.find('table', attrs={'id': 'product-dollars'})
        list_of_headers = []
        list_of_cells = []

        for row in product_dollars.find_all('tr'):
            for header in row.find_all('th'):
                header_content = header.get_text()
                clean_headers = re.sub( '\r\n', ' ', header_content).strip()
                clean_headers2 = re.sub( '\n\n', ' ', clean_headers).strip()
                list_of_headers.append(clean_headers2)

            for value in row.find_all('td'):
                value_content = value.get_text()
                clean_values = re.sub( '\r\n', ' ', value_content).strip()
                clean_values2 = re.sub( '\n\n', ' ', clean_values).strip()
                list_of_cells.append(clean_values2)

        counter = 0
        for h in list_of_headers:
            dic[h] = list_of_cells[counter]
            counter = counter + 1

        return dic

    def scrapePartId(self, soup, dic):
        inputTag = soup.find("input", attrs={"name" : "partid"})
        return inputTag["value"]

    def available(self, dic):
        if (dic['Quantity Available'] == '0'):
            return False
        else:
            return True

    def makeLeadTimeRequest(self, dic, part_id):
         headers = {"Content-type": "application/x-www-form-urlencoded"}
         conn = http.client.HTTPSConnection("www.digikey.com")
         tempJSON = {
            "language":"en",
            "partid": part_id,
            "quantity": dic['Price Break']
         }
         params = json.dumps(tempJSON)
         conn.request("POST", "/product-detail/leadtime/en/", params, headers)
         response = conn.getresponse()
         print(response)


    def filterHeaders(self, dic):
        tempDic = {}
        for i in self.__headers:
            key = i
            if key in dic:
                tempDic[key] = dic[key]
            else:
                tempDic[key] = "N/A"
        return tempDic

    def writeToCSV(self, filename, list_of_parts):
        with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.__headers)
                writer.writeheader()

                for i in list_of_parts:
                    writer.writerow(i)

    def printListItems(li):
        for i in li:
            print(i)

    def printList(l):
        print (l)
