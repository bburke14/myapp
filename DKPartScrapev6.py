from bs4 import BeautifulSoup
import requests
import csv
import re

master_list_of_headers = []
once = False

def readUrlList():
    templist = []
    with open('test_list_of_urls.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, line in enumerate(reader):
            for key in line:
                templist.append(line[key])
    return templist

def getdatsoup(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def printList(li):
    for i in li:
        print(i)


def scrapebabyscrape(soup):
    content = soup.find('div', attrs={'id': 'pdp_content'})
    tophalf = content.find('div', attrs={'id': 'tophalf'})
    productdetails1 = tophalf.find('table', attrs={'id': 'product-details'})
    list_of_headers = []
    list_of_cells = []
    dic = {}
    for row in productdetails1.find_all('tr'):
        for header in row.find_all('th'):
            header_content = header.get_text()
            clean_headers = re.sub( '\r\n', ' ', header_content).strip()
            clean_headers2 = re.sub( '\n\n', ' ', clean_headers).strip()
            list_of_headers.append(clean_headers2)
            if once == False:
                master_list_of_headers.append(clean_headers2)
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




url_list = readUrlList()
list_of_parts = []
for url in url_list:
    res = getdatsoup(url)
    list_of_parts.append(scrapebabyscrape(res))
    once = True
print(list_of_parts)

with open('DKPartScrapev6.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=master_list_of_headers)
        writer.writeheader()

        for i in list_of_parts:
            writer.writerow(i)






#
# rightcolumn = content.find('div', attrs={'id': 'rightcolumn'})
# productdetails2 = rightcolumn.find('table', attrs={'id': 'product-dollars'})
#
# prices = productdetails2.find_all('td')
# for price in prices
#
# print(prices)
