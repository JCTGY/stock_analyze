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


#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style
#import import_data as imp

# Adjusting the size of matplotlib
import matplotlib as mpl
from pandas.plotting import scatter_matrix

#mavg = imp.mavg
#close_px = imp.close_px
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
#style.use('ggplot')

#close_px.plot(label='AAPL')
#mavg.plot(label='mavg')

#rets = close_px / close_px.shift(1) - 1
#rets.plot(label='return')
#plt.legend()
#plt.show()

dfcomp = web.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],'yahoo',start=start,end=end)['Adj Close']
retscomp = dfcomp.pct_change()

corr = retscomp.corr()
#plt.scatter(retscomp.AAPL, retscomp.GE)
#plt.xlabel('Returns AAPL')
#plt.ylabel('Returns GE')

#scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10));

#plt.imshow(corr, cmap='hot', interpolation='none')
#plt.colorbar()
#plt.xticks(range(len(corr)), corr.columns)
#plt.yticks(range(len(corr)), corr.columns);

plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
plt.show()

