import matplotlib as mpl
mpl.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
from statsmodels.tsa.stattools import coint, adfuller

import io
import base64
import sqlite3


def fetch_data(asset, dataset, startdate, enddate):
    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM piperdb", conn, index_col = 'date', parse_dates=True)
    data = df.loc[startdate:enddate]
    pivot_table = data.pivot(columns='symbol',
                             values=dataset)
    filtered_data = pivot_table.filter(items=asset)
    return filtered_data

def zscore(series):
    return (series - series.mean()) / np.std(series)

def draw_chart(symbol_list, start_date, end_date):
    # Hämta data ur historisk databas+livedatabas
    price = fetch_data(symbol_list, 'closing_price', start_date, end_date)

    # Separera listan till två variabler
    S1 = price[symbol_list[0]]
    S2 = price[symbol_list[1]]

    # Beräkna spread
    S1 = sm.add_constant(S1)
    results = sm.OLS(S2.astype(float), S1.astype(float)).fit()
    S1 = S1[symbol_list[0]]  # återställer S1
    b = results.params[symbol_list[0]]
    spread = S2 - b * S1

    # Beräkna omvänd spread
    S2 = sm.add_constant(S2)
    results = sm.OLS(S1.astype(float), S2.astype(float)).fit()
    S2 = S2[symbol_list[1]]  # återställer S2
    b = results.params[symbol_list[1]]
    spread_rev = S1 - b * S2

    zscore1 = zscore(spread)
    zscore2 = zscore(spread_rev)

    score, pvalue, _ = coint(S1.astype(float), S2.astype(float))
    pvalue = round(pvalue, 4)
    if pvalue <= 0.05:
        coint_string = ('p-Value = ' + str(pvalue) + ' Likely cointegrated')
    else:
        coint_string = ('p-Value = ' + str(pvalue) + ' Likely NOT cointegrated')

    #plotta Zscore
    zscore1.plot(linewidth=1.7, figsize=(10, 2))
    zscore2.plot(linewidth=1.7)
    plt.xlabel('')
    plt.axhline(zscore(spread).mean(), color='black', linewidth=1.0)
    plt.axhline(1.0, color='red', linestyle='--', linewidth=1.0)
    plt.axhline(-1.0, color='green', linestyle='--', linewidth=1.0)
    plt.axhline(2.0, color='grey', linestyle='--', linewidth=.5)
    plt.axhline(-2.0, color='grey', linestyle='--', linewidth=.5)
    plt.title(coint_string, loc='left', color='white', fontsize=10);
    plt.xticks(rotation=0, color='white', fontsize=8)
    plt.yticks(color='white', fontsize=8)
    plt.legend([symbol_list[1], symbol_list[0]], bbox_to_anchor=(1.0, 1.12), loc=5,
               ncol=2, borderaxespad=0.);

    f = io.BytesIO()

    plt.savefig(f,
                format="png",
                facecolor=('#3d5c87'),
                bbox_inches='tight',
                )
    plt.clf()

    image_b64 = base64.b64encode(f.getvalue())  # konverterar bilden till base64
    image_show = str(image_b64, 'utf8')  # encodar till 8 bit strängar

    return image_show