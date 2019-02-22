import requests
from bs4 import BeautifulSoup as soup
import datetime
import time
from piperdatabase.models import PiperDatabase
from .symbols import symbolUrl, symbolList


def scrape_live(asset):
    url = requests.get('https://www.investing.com/' + symbolUrl[asset],
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
    url = requests.get('https://www.investing.com/' + symbolUrl[asset],
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

    for symbol in symbolList:
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

    update_live_message = 'databas uppdaterades.'
    return update_live_message


def updatehistoricaldb(historical_date):
    now = datetime.datetime.now()

    PiperDatabase.objects.filter(date=historical_date).delete()

    for symbol in symbolList:
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

    update_historical_message = 'databas uppdaterades med data för ' + str(historical_date) + '.'
    return update_historical_message
