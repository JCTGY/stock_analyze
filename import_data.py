import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 9, 1)

df = web.DataReader("AAPL", 'yahoo', start, end)
df.tail()

# moving average for last 100 windows
close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()

