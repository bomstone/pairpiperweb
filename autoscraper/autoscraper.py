import sqlite3
import requests
from bs4 import BeautifulSoup as soup
import datetime
import time
import os
from ppconfig import db_name, symbolDict


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file = os.path.join(BASE_DIR, 'autoscraper/log.txt')


def append_to_log(counter, script_time):
    log_txt = open(str(log_file), 'a')

    now = datetime.datetime.now()
    time_stamp = now.strftime('%Y-%m-%d %H:%M:%S')
    script_time = script_time.total_seconds()
    log_txt.write(str(time_stamp) + ' - Finished adding ' + str(counter) +
                  ' rows to ' + str(db_name) + '. Script execution time: ' + str(script_time) + 's\n')

    log_txt.close()


def scrape_investing_com(symbol):
    url = requests.get('https://www.investing.com/' + symbolDict[symbol],
                       headers={'User-Agent': 'Mozilla/5.0 Chrome/70.0.3538.110'})
    page_soup = soup(url.content, 'html.parser')
    containers = page_soup.findAll('table', {'class': 'genTbl closedTbl historicalTbl'})

    livedata = []
    i = 0

    for table in containers:
        for td in table.findAll('td'):
            if i >= 5:
                break
            i += 1
            livedata.append(td.text)

    datetime_object = datetime.datetime.strptime(livedata[0], '%b %d, %Y').date()
    parse_date = (str(datetime_object))
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    datastring = [parse_date,
                  symbol,
                  livedata[2].replace(',', ''),
                  livedata[3].replace(',', ''),
                  livedata[4].replace(',', ''),
                  livedata[1].replace(',', ''),
                  timestamp
                  ]
    url.close()
    time.sleep(2)
    return datastring


def collect_data():
    collected_set = []
    now = datetime.datetime.now()

    for symbol in symbolDict:
        row = scrape_investing_com(symbol)
        row[0] = now.strftime('%Y-%m-%d')
        collected_set.append(row)

    return collected_set


def update_piperdb():
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    counter = 0

    conn = sqlite3.connect(str(db_name))
    c = conn.cursor()
    c.execute("DELETE FROM piperdb WHERE date=(?)", (date,))
    conn.commit()
    conn.close()
    dataset = collect_data()
    script_time = datetime.datetime.now() - now

    for row in dataset:

        conn = sqlite3.connect(str(db_name))
        c = conn.cursor()
        c.execute("""INSERT INTO piperdb (date, symbol, opening_price, high_price, low_price, closing_price, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)""", (
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            ))
        counter += 1
        conn.commit()
    conn.close()

    append_to_log(counter, script_time)


update_piperdb()


