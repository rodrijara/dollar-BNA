#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

url = 'https://www.bna.com.ar'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

pane = soup.find('div', class_='tab-pane fade in active')
rates = pane.table.tbody.text

rates_list = rates.split()

print(rates_list)