#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from connections import create_connection, execute_query

url = 'https://www.bna.com.ar'
response = requests.get(url)

# scrapping the url
soup = BeautifulSoup(response.text, 'lxml')
pane = soup.find('div', class_='tab-pane fade in active')
rates = pane.table.tbody.text
date = pane.table.thead.text

# get rates values
_, _, usd_c, usd_v, _, eur_c, eur_v, *others = rates.split()
date= date.split()[0]

# stablish a SQLite connection and save the data

print('... Connecting DB')

connection = create_connection('./ratesDB')

print('... Creating new table')

create_rates_table = """
CREATE TABLE rates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT NOT NULL UNIQUE,
usd_c REAL,
usd_v REAL,
eur_c REAL, 
eur_v REAL
);
"""
execute_query(connection, create_rates_table)

print('... Saving todays\' date and values in DB')

save_rates = """
INSERT INTO 
rates (date, usd_c, usd_v, eur_c, eur_v)
VALUES
(?, ?, ?, ?, ?)"""
execute_query(connection, save_rates, date, usd_c, usd_v, eur_c, eur_v)
