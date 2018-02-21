import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.digikey.com/products/en/capacitors/tantalum-capacitors/59?k=&pkeyword=&FV=ffe0003b%2Cfffc018f&quantity=0&ColumnSort=0&page=1&pageSize=500'
with
response = requests.get(url)
# html = response.content
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'id': 'lnkPart'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

print(list_of_rows)
# outfile = open('.\digikeyscrape2.csv', 'w')
# writer = csv.writer(outfile)
# writer.writerows(list_of_rows)

# print(list_of_rows)

    #     text = cell.text.replace('&nbsp;', '')
    #     list_of_cells.append(text)
    # list_of_rows.append(list_of_cells)

# outfile = open("./digikeyscrape.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerows(list_of_rows)



#for row in table.find('tr'):
#    print(row.prettify())
#row = soup.find('tr', attrs={'itemtype': 'http://schema.org/Product'})

#print(table.prettify())

#soup.find_all('tr', attrs={'itemtype': 'http://schema.org/Product'}))
###tr is the row, td is the cell in the table.
