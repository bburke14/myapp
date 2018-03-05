from bs4 import BeautifulSoup
import requests
import csv
import re
import http.client, urllib.parse
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
            if h == 'Quantity Available':
                temp = list_of_cells[counter]
                if temp[0] == '0':
                    dic[h] = '0'
                else:
                    dic[h] = list_of_cells[counter]
            else:
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
        url = "https://www.digikey.com/product-detail/leadtime/en/"
        quantity = dic['Price Break']
        quantity = quantity.replace(',', '')
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\nen\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"partid\"\r\n\r\n" + str(part_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"quantity\"\r\n\r\n" + str(quantity) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Cache-Control': "no-cache",
        'Postman-Token': "5e45fd65-e678-1653-11f3-8af451116857"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return response.text


    def getShipDate(self, dic, html):
        soup = BeautifulSoup(html, 'html.parser')
        ship = soup.find('table', attrs={'id': 'leadTimeTable'})

        rows = ship.find_all('tr')
        headers = rows[1].find_all('td')
        val = headers[1].get_text()

        if val != '*':
            dic['Ship Date Estimate'] = val

        return dic


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
