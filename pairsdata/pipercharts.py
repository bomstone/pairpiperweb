import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from django.core.files.storage import default_storage

def fetch_data(asset, dataset, startdate, enddate):
    df = pd.read_csv('fulldb.csv', index_col = 'date', parse_dates=True).append(pd.read_csv('livedb.csv', index_col = 'date', parse_dates=True))
    data = df.loc[startdate:enddate]
    pivot_table = data.pivot(columns='symbol',
                             values=dataset)
    filtered_data = pivot_table.filter(items=asset)
    return filtered_data

def zscore(series):
    return (series - series.mean()) / np.std(series)

def plot_chart(symbol_list, start_date, end_date):
    #Hämta data ur historisk databas+livedatabas
    price = fetch_data(symbol_list, 'closing_price', start_date, end_date)

    #Separera listan till två variabler
    S1 = price[symbol_list[0]]
    S2 = price[symbol_list[1]]

    #Beräkna spread
    S1 = sm.add_constant(S1)
    results = sm.OLS(S2, S1).fit()
    S1 = S1[symbol_list[0]]   #återställer S1
    b = results.params[symbol_list[0]]
    spread = S2 - b * S1

        #Beräkna omvänd spread
    S2 = sm.add_constant(S2)
    results = sm.OLS(S1, S2).fit()
    S2 = S2[symbol_list[1]]   #återställer S2
    b = results.params[symbol_list[1]]
    spread_rev = S1 - b * S2

    #Beräkna och plotta Zscore
    zscore(spread).plot(figsize=(16,3))
    zscore2 = zscore(spread_rev)
    zscore2.plot(figsize=(16,3))
    plt.axhline(zscore(spread).mean(), color='black')
    plt.axhline(1.0, color='red', linestyle='--')
    plt.axhline(-1.0, color='green', linestyle='--')
    plt.legend(['Spread ' + symbol_list[1], 'Spread ' + symbol_list[0]], bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=1, mode="expand", borderaxespad=0.);
    #plt.savefig('assets/fig.png')