import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick2_ohlc
import mpl_finance
import pandas_datareader.data as web
import datetime

import matplotlib.ticker as ticker


start = datetime.datetime(2020,7,1)
end = datetime.datetime(2020,8,1)
sk_hynix=web.DataReader('000660.KS','yahoo',start,end)
sk_hynix=sk_hynix[sk_hynix['Volume']>0]

fig = plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)
day_list=[]
name_list=[]
for i,day in enumerate(sk_hynix.index):
    if day.dayofweek ==0:  # 월요일 판별
        day_list.append(i)
        name_list.append(day.strftime('%m-%d')+('Mon'))

ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))
ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
candlestick2_ohlc(ax,sk_hynix['Open'],sk_hynix['High'],sk_hynix['Low'],sk_hynix['Close'],width=0.5,colorup='r',colordown='b')
'''
top_axes = plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
bottom_axes = plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=4)

top_axes.plot(sk_hynix.index,sk_hynix['Close'], label = 'Close')
bottom_axes.plot(sk_hynix.index,sk_hynix['Volume'],label = 'Vol')
'''
plt.tight_layout()

plt.show()