from bs4 import BeautifulSoup
import requests
import csv
import re

url = 'https://www.digikey.com/products/en/capacitors/tantalum-capacitors/59?k=&pkeyword=&FV=ffe0003b%2Cfffc018f&quantity=0&ColumnSort=0&page=1&pageSize=500'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs={'id': 'productTable'})

rows = table.findChildren('tr')

list_of_rows = []
for row in rows:
    cells = row.findChildren('td')
    list_of_cells = []
    for cell in cells:
        cell_content = cell.getText()
        clean_content = re.sub( '\s+', ' ', cell_content).strip()
        print(clean_content)

outfile = open('.\digikeyscrape2.csv', 'w')
writer = csv.writer(outfile)
writer.writerows(clean_content)

# list_of_rows = []
# for row in table.findAll('tr')[1:]:


#     list_of_cells = []
#     cellz = row.findAll('td', attrs={'class': 'tr-description'})
#     for cell in row.findAll('a'):
#         text = cell.text.replace('&nbsp', '')
#         list_of_cells.append(text)
#
#
#
#     list_of_rows.append(list_of_cells)
# desc = soup.findAll('td', attrs={'class': 'tr-description'})
# print(desc)
#
#
# outfile = open('.\digikeyscrape2.csv', 'w')
# writer = csv.writer(outfile)
# writer.writerows(list_of_rows)

# print(list_of_rows)
