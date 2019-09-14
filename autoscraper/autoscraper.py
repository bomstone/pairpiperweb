import sqlite3
import requests
from bs4 import BeautifulSoup as soup
import datetime
import time
from config import symbol_dict
from config import db_name
from config import log_file

def append_to_log(counter, script_time):
    log_txt = open(str(log_file), 'a')

    now = datetime.datetime.now()
    time_stamp = now.strftime('%Y-%m-%d %H:%M:%S')
    script_time = script_time.total_seconds()
    log_txt.write(str(time_stamp) + ' - Finished adding ' + str(counter) +
                  ' rows to ' +str(db_name) + '. Script execution time: ' + str(script_time) + 's\n')

    log_txt.close()

def scrape_live(symbol):
    url = requests.get('https://www.investing.com/' + symbol_dict[symbol],
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
    datastring = [parse_date,
                  symbol,
                  livedata[2].replace(',', ''),
                  livedata[3].replace(',', ''),
                  livedata[4].replace(',', ''),
                  livedata[1].replace(',', ''),
                  ]
    url.close()
    time.sleep(2)
    return datastring

def updatelivedb():
    now = datetime.datetime.now()
    conn = sqlite3.connect(str(db_name))
    c = conn.cursor()

    date = now.strftime('%Y-%m-%d')
    c.execute("DELETE FROM piperdb WHERE date=(?)", (date,))

    conn.commit()
    conn.close()
    counter = 0
    for symbol in symbol_dict:

        time_stamp = now.strftime('%Y-%m-%d %H:%M:%S')
        row = scrape_live(symbol)
        row[0] = now.strftime('%Y-%m-%d')

        conn = sqlite3.connect(str(db_name))
        c = conn.cursor()
        c.execute("""INSERT INTO piperdb (date, symbol, opening_price, high_price, low_price, closing_price, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)""", (
            row[0], 
            row[1], 
            row[2], 
            row[3], 
            row[4], 
            row[5],
            time_stamp,
            ))

        counter += 1
        conn.commit()

    conn.close()

    script_time = datetime.datetime.now() - now

    append_to_log(counter, script_time)

updatelivedb()




