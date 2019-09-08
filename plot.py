#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style
import import_data as imp

# Adjusting the size of matplotlib
import matplotlib as mpl


mavg = imp.mavg
close_px = imp.close_px
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()
