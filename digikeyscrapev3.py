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

def get_dem_headers(url):
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
    return header_list



def scrape_baby_scrape(url):
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
    print(list_of_rows)

def write_to_csv(url):
    for item in list_of_rows:
        writer.writerow(item)


with open('.\digikeyscrape3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, lineterminator = "\n")


    for url in url_list:
        res = scrape_baby_scrape(url)
        write_to_csv(res)
