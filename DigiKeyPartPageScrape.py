import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.digikey.com/product-detail/en/kemet/T520V337M004ATE007/399-4656-2-ND/992047'

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', attrs={'id': 'product-details'})

form = table.find('span', attrs={'id': 'leadtime-dis'})

print(form.prettify())
