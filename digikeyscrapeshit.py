from bs4 import BeautifulSoup
import requests
import csv
import re

url = 'https://www.digikey.com/products/en/capacitors/tantalum-capacitors/59?k=&pkeyword=&FV=ffe0003b%2Cfffc018f&quantity=0&ColumnSort=0&page=1&pageSize=500'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs={'id': 'productTable'})

headers = table.findChildren('th')

header_list = []
for header in headers:
    header_content = header.getText()
    clean_headers = re.sub( '\r\n', ' ', header_content).strip()
    clean_headers2 = re.sub( '\n\n', ' ', clean_headers).strip()
    if clean_headers2 != '':
        if clean_headers2 != 'Compare Parts':
            if clean_headers2 != 'Image':
                header_list.append(clean_headers2)

print(header_list)

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



with open('.\digikeyscrape2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator = "\n")
    writer.writerow(header_list)
    for item in list_of_rows:
        writer.writerow(item)
