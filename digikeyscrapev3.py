from bs4 import BeautifulSoup
import requests
import csv
import re

def readUrlList():
    tempList = []
    with open('digikeyurllist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, line in enumerate(reader):
            for key in line:
                tempList.append(line[key])
    return tempList

url_list = readUrlList()
print(url_list)


def scrape_baby_scrape(url):
    url = 'https://www.digikey.com/products/en/capacitors/tantalum-capacitors/59?k=&pkeyword=&pv7=2&pv1989=0&FV=fffc018f%2Cffe0003b&quantity=0&ColumnSort=0&page=1&pageSize=500'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', attrs={'id': 'productTable'})

    rows = table.findChildren('tr')
    outfile = open('.\digikeyscrape2.csv', 'wb')

    list_of_rows = []
    for row in rows:
        cells = row.findChildren('td')
        list_of_cells = []
        for cell in cells:
            cell_content = cell.getText()
            clean_content = re.sub( '\s+', ' ', cell_content).strip()
            if clean_content != '':
                list_of_cells.append(clean_content)
        list_of_rows.append(list_of_cells)
    return



with open('.\digikeyscrape3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator = "\n")
    writer.writerow(header_list)

    #for url in url_list:
