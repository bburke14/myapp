from bs4 import BeautifulSoup
import requests
import csv
import re

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

def scrapebabyscrape(soup):
    content = soup.find('div', attrs={'id': 'pdp_content'})
    tophalf = content.find('div', attrs={'id': 'tophalf'})
    productdetails1 = tophalf.find('table', attrs={'id': 'product-details'})
    for row in productdetails1.find_all('tr'):
        productid = row.findChildren('td', attrs={'id': 'reportPartNumber'})
        quantityavailable = row.findChildren('span', attrs={'id': 'dkQty'})
        manupartnum = row.findChildren('meta', attrs={'itemprop': 'name'})
        print(productid, quantityavailable)
    rightcolumn = content.find('div', attrs={'id': 'rightcolumn'})
    productdetails2 = rightcolumn.find('table', attrs={'id': 'product-dollars'})
    for row in productdetails2.find_all('tr'):
        price = productdetails2.findChildren('td', attrs={'span': 'price'})
        print(price)

        # for header in row.find_all('th'):
        #     for value in row.find_all('td'):
        #         header_content = header.get_text()
        #         clean_headers = re.sub( '\r\n', ' ', header_content).strip()
        #         clean_headers2 = re.sub( '\n\n', ' ', clean_headers).strip()
        #         value_content = value.get_text()
        #         clean_values = re.sub( '\r\n', ' ', value_content).strip()
        #         clean_values2 = re.sub( '\n\n', ' ', clean_values).strip()
        #         print(clean_headers2, clean_values2)


# with open('DKPartScrapev5.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         url_list = readUrlList()

        # for url in url_list:
        #     res = getdatsoup(url)
        #     details = scrapebabyscrape(res)
        #     writer.writerow(res)

url_list = readUrlList()

for url in url_list:
    res = getdatsoup(url)
    details = scrapebabyscrape(res)








#
# rightcolumn = content.find('div', attrs={'id': 'rightcolumn'})
# productdetails2 = rightcolumn.find('table', attrs={'id': 'product-dollars'})
#
# prices = productdetails2.find_all('td')
# for price in prices
#
# print(prices)
