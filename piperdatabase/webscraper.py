import requests
from bs4 import BeautifulSoup as soup
import datetime
import sqlite3
import time
from piperdatabase.models import PiperDatabase


symbol_list = [
    'ABB',
    'ALFA',
    'ALIV-SDB',
    'ASSA-B',
    'ATCO-A',
    'ATCO-B',
    'AXFO',
    'BOL',
    'CAST',
    'DAX',
    'ELUX-B',
    'EURSEK',
    'FABG',
    'GLD',
    'HOLM-B',
    'HUFV-A',
    'HUSQ-B',
    'ICA',
    'NCC-B',
    'NDA-SEK',
    'NIBE-B',
    'OMX',
    'PEAB-B',
    'SAAB-B',
    'SAND',
    'SCA-B',
    'SEB-A',
    'SECU-B',
    'SHB-A',
    'SKA-B',
    'SKF-A',
    'SKF-B',
    'SLV',
    'SP500',
    'SSAB-A',
    'SSAB-B',
    'STE-R',
    'SWED-A',
    'TEL2-B',
    'TELIA',
    'TREL-B',
    'USDSEK',
    'VIX',
    'VOLV-A',
    'VOLV-B',
]

asset_url = {
    'ABB': 'equities/abb-ltd-historical-data?cid=482',
    'ALFA': 'equities/alfa-laval-historical-data',
    'ALIV-SDB': 'equities/autoliv-inc-historical-data',
    'ASSA-B': 'equities/assa-abloy-historical-data',
    'ATCO-A': 'equities/atlas-copco-a-historical-data',
    'ATCO-B': 'equities/atlas-copco-b-historical-data',
    'AXFO': 'equities/axfood-ab-historical-data',
    'BOL': 'equities/boliden-historical-data',
    'CAST': 'equities/castellum-ab-historical-data?cid=25979',
    'DAX': 'indices/germany-30-historical-data',
    'ELUX-B': 'equities/electrolux-b-historical-data',
    'EURSEK': 'currencies/eur-sek-historical-data',
    'FABG': 'equities/fabege-historical-data?cid=25983',
    'GLD': 'etfs/spdr-gold-trust-historical-data',
    'HOLM-B': 'equities/holmen-historical-data?cid=25987',
    'HUFV-A': 'equities/hufvudstaden-historical-data?cid=25988',
    'HUSQ-B': 'equities/husqvarna-b-historical-data?cid=25990',
    'ICA': 'equities/hakon-invest-historical-data?cid=25985',
    'NCC-B': 'equities/ncc-b-historical-data?cid=26008',
    'NDA-SEK': 'equities/nordea-bank-finland-historical-data?cid=9013',
    'NIBE-B': 'equities/nibe-industrier-b-historical-data',
    'OMX': 'indices/omx-stockholm-30-historical-data',
    'PEAB-B': 'equities/peab-ab-historical-data?cid=26011',
    'SAAB-B': 'equities/saab-ab-historical-data?cid=26013',
    'SAND': 'equities/sandvik-historical-data',
    'SCA-B': 'equities/svenska-cell-historical-data',
    'SEB-A': 'equities/s.e.b-historical-data',
    'SECU-B': 'equities/securitas-b-historical-data',
    'SHB-A': 'equities/svenska-handelsbanken-historical-data',
    'SKA-B': 'equities/skanska-b-historical-data',
    'SKF-A': 'equities/skf-historical-data',
    'SKF-B': 'equities/skf-b-historical-data',
    'SLV': 'etfs/ishares-silver-trust-historical-data',
    'SP500': 'indices/us-spx-500-historical-data',
    'SSAB-A': 'equities/ssab-historical-data',
    'SSAB-B': 'equities/ssab-ab-historical-data?cid=26018',
    'STE-R': 'equities/stora-enso-exch-historical-data',
    'SWED-A': 'equities/swedbank-historical-data',
    'TEL2-B': 'equities/tele2-historical-data',
    'TELIA': 'equities/teliasonera-historical-data',
    'TREL-B': 'equities/trelleborg-historical-data?cid=26020',
    'USDSEK': 'currencies/usd-sek-historical-data',
    'VIX': 'indices/volatility-s-p-500-historical-data',
    'VOLV-A': 'equities/volvo-a-historical-data?cid=26021',
    'VOLV-B': 'equities/volvo-b-historical-data',
}

def scrape_live(asset):
    url = requests.get('https://www.investing.com/' + asset_url[asset],
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
                  asset,
                  livedata[2].replace(',', ''),
                  livedata[3].replace(',', ''),
                  livedata[4].replace(',', ''),
                  livedata[1].replace(',', ''),
                  ]
    url.close()
    time.sleep(2)
    return datastring

def scrape_historical(asset, date_input):
    # konverterar angivet datum yyyy-mm-dd till Xxx dd, yyyy för att kunna matchas på investing.com
    datetime_first_converter = datetime.datetime.strptime(date_input, '%Y-%m-%d')
    conv_date_string = datetime.datetime.date(datetime_first_converter)
    converted_date = conv_date_string.strftime("%b %d, %Y")

    # Öppnar historisk data för 'asset' på investing.com
    url = requests.get('https://www.investing.com/' + asset_url[asset],
                       headers={'User-Agent': 'Mozilla/5.0 Chrome/70.0.3538.110'})
    page_soup = soup(url.content, 'html.parser')
    containers = page_soup.findAll('table', {
        'class': 'genTbl closedTbl historicalTbl'})  # lagrar tabellen med historisk data i 'containers'

    # lagrar varje rad i tabellen i list-variabeln 'scraped_data'
    scraped_data = []
    for table in containers:
        for td in table.findAll('td'):
            scraped_data.append(td.text)

    position = scraped_data.index(converted_date)  # letar upp och returnerar positionen för angivet datum
    steps = 5  # anger hur många steg som ska returneras (5 = datum, price, open, high, low)

    filtered_data = scraped_data[position:position + steps]  # filtrerar tabellen enligt ovanstående

    # formaterar datum till yyyy-mm-dd, samt organiserar om ordningen i output till 'datum, asset, open, high, low, close'
    datetime_object = datetime.datetime.strptime(filtered_data[0], '%b %d, %Y').date()
    parse_date = (str(datetime_object))
    datastring = [parse_date,
                  asset,
                  filtered_data[2].replace(',', ''),
                  filtered_data[3].replace(',', ''),
                  filtered_data[4].replace(',', ''),
                  filtered_data[1].replace(',', ''),
                  ]
    url.close()
    time.sleep(2)
    return datastring

def updatelivedb():
    now = datetime.datetime.now()

    PiperDatabase.objects.filter(date=now.strftime('%Y-%m-%d')).delete()

    for symbol in symbol_list:
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        row = scrape_live(symbol)
        row[0] = now.strftime('%Y-%m-%d')

        add = PiperDatabase(
            date = row[0],
            symbol = row[1],
            opening_price = row[2],
            high_price = row[3],
            low_price = row[4],
            closing_price = row[5],
            timestamp = timestamp,
        )
        add.save()

    update_live_message = 'livedb.csv uppdaterades.'
    return update_live_message


def updatehistoricaldb(historical_date):
    now = datetime.datetime.now()

    PiperDatabase.objects.filter(date=historical_date).delete()

    for symbol in symbol_list:
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        row = scrape_historical(symbol, historical_date)

        add = PiperDatabase(
            date=row[0],
            symbol=row[1],
            opening_price=row[2],
            high_price=row[3],
            low_price=row[4],
            closing_price=row[5],
            timestamp=timestamp,
        )
        add.save()

    update_historical_message = 'fulldb.csv uppdaterades med data för ' + str(historical_date) + '.'
    return update_historical_message
