import requests
import json
import pprint
from datetime import date, datetime

USDX_CURRENCY_BASKET = [['EUR', 57.6], ['JPY', 13.6], ['GBP', 11.9], ['CAD', 9.1], ['SEK', 4.2], ['CHF', 3.6]]

# base currency or reference currency
base = "USD"

# # required currency for plot
# out_curr="EUR"

answer = input('Ввести дані самостійно - введіть "1", ініціалізувати тестовий приклад - будь-яка клавіша')

start_date, end_date = '', ''

if (answer == '1'):
    print('Set start date')
    start_year = int(input('Enter a year: '))
    start_month = int(input('Enter a month: '))
    start_day = int(input('Enter a day: '))
    start_date = date(start_year, start_month, start_day)

    print('Set end date')
    end_year = int(input('Enter a year: '))
    end_month = int(input('Enter a month: '))
    end_day = int(input('Enter a day: '))
    end_date = date(end_year, end_month, end_day)
else:
    start_date = "2021-01-01"
    end_date = "2021-03-04"

counter = 0
# api url for request
while counter < len(USDX_CURRENCY_BASKET):
    url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(
        USDX_CURRENCY_BASKET[counter][0], start_date, end_date, base)
    response = requests.get(url)
    data = response.json()
    rates = []
    # extract dates and rates from each item of dictionary or json in the above created list
    for i, j in data["rates"].items():
        rates.append([i, j[base]])

    USDX_CURRENCY_BASKET[counter].append(rates)
    counter += 1

import pandas as pd

df = pd.DataFrame(rates)
# define column names explicitely
df.columns = ["date", "rate"]

x = df['date']
# Put exchange rates on the y-axis
y = df['rate']


import time
import psutil
import matplotlib.pyplot as plt


%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

plt.xticks(rotation=90)
plt.title("Сurrency rates")
plt.xlabel('Date', fontsize=12)
plt.ylabel('Exchange Rates', fontsize=12)

# fig_basket_value = plt.figure()
# ax_basket = fig.add_subplot(111)
# fig_basket_value.show()
# plt.xticks(rotation=90)
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Currency basket price', fontsize=12)

i = 0
eur_x_result, eur_y_result = [], []
gpy_x_result, gpy_y_result = [], []
gbp_x_result, gbp_y_result = [], []
cad_x_result, cad_y_result = [], []
sek_x_result, sek_y_result = [], []
chf_x_result, chf_y_result = [], []

EUR_DF, JPY_DF, GBP_DF, CAD_DF, SEK_DF, CHF_DF = pd.DataFrame(USDX_CURRENCY_BASKET[0][2]), pd.DataFrame(
    USDX_CURRENCY_BASKET[1][2]), pd.DataFrame(USDX_CURRENCY_BASKET[2][2]), pd.DataFrame(
    USDX_CURRENCY_BASKET[3][2]), pd.DataFrame(USDX_CURRENCY_BASKET[4][2]), pd.DataFrame(USDX_CURRENCY_BASKET[5][2])

EUR_DF.columns = ["date", "rate"]
JPY_DF.columns = ["date", "rate"]
GBP_DF.columns = ["date", "rate"]
CAD_DF.columns = ["date", "rate"]
SEK_DF.columns = ["date", "rate"]
CHF_DF.columns = ["date", "rate"]

EUR_X, EUR_Y = EUR_DF['date'], EUR_DF['rate']
JPY_X, JPY_Y = JPY_DF['date'], JPY_DF['rate']
GBP_X, GBP_Y = GBP_DF['date'], GBP_DF['rate']
CAD_X, CAD_Y = CAD_DF['date'], CAD_DF['rate']
SEK_X, SEK_Y = SEK_DF['date'], SEK_DF['rate']
CHF_X, CHF_Y = CHF_DF['date'], CHF_DF['rate']

while i < len(x):
    eur_x_result.append(EUR_X[i])
    eur_y_result.append(EUR_Y[i])

    gpy_x_result.append(JPY_X[i])
    gpy_y_result.append(JPY_Y[i])

    gbp_x_result.append(GBP_X[i])
    gbp_y_result.append(GBP_Y[i])

    cad_x_result.append(CAD_X[i])
    cad_y_result.append(CAD_Y[i])

    sek_x_result.append(SEK_X[i])
    sek_y_result.append(SEK_Y[i])

    chf_x_result.append(CHF_X[i])
    chf_y_result.append(CHF_Y[i])

    ax.plot(eur_x_result, eur_y_result, color='b')
    #     ax.plot(gpy_x_result, gpy_y_result, color='r')

    fig.canvas.draw()

    time.sleep(0.5)
    i += 1


