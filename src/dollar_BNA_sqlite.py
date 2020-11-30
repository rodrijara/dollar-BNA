#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from connections_sqlite import create_connection, execute_query

url = 'https://www.bna.com.ar'
source = requests.get(url).text

# scrapping the url
soup = BeautifulSoup(source, 'lxml')
pane = soup.find('div', class_='tab-pane fade in active')
rates = pane.table.tbody.text
date = pane.table.thead.text

# get rates values
_, _, usd_c, usd_v, *others = rates.split()
date= date.split()[0]

# stablish a SQLite connection and save the data

print('... Connecting DB')

connection = create_connection('./BNA-dollar-DB')

print('... Creating new table')

create_rates_table = """
CREATE TABLE rates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT NOT NULL UNIQUE,
usd_c REAL,
usd_v REAL
);
"""
execute_query(connection, create_rates_table)

print('... Saving todays\' date and values in DB')

save_rates = """
INSERT INTO 
rates (date, usd_c, usd_v)
VALUES
(?, ?, ?, ?, ?)"""
execute_query(connection, save_rates, date, usd_c, usd_v)
