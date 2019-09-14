# AUTOSCRAPER CONFIG

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# coding=utf-8
#databas - ange komplett sökväg till databas
db_name = os.path.join(BASE_DIR, 'db.sqlite3')
#logfil - ange komplett sökväg till logfil
log_file = os.path.join(BASE_DIR, 'autoscraper/log.txt')

# Symboler med respektive URL på https://www.investing.com/'
symbol_dict = {
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

symbolList = list(symbol_dict.keys())