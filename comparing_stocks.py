import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as web
from matplotlib import style
import datetime as dt

style.use('ggplot')
start = dt.datetime(2017, 1, 1)
end = dt.datetime(2019, 1, 1)

# apple=web.DataReader('AAPL','yahoo',start,end)
# facebook = web.DataReader('FB','yahoo',start,end)

# save to a file
# apple.to_json('apple2019.json')
# facebook.to_json('facebook2019.json')


# load from a file
apple = pd.read_json('./apple2019.json')
facebook = pd.read_json('./facebook2019.json')

apple['Adj Close'].plot(label= 'AAPL')
facebook['Adj Close'].plot(label='FB')
# Notice that we are specifying a label , which is important for the legend that helps us to
# distinguish between the two companies.

plt.ylabel('Adjusted CLose')
plt.title('Share Price')
plt.legend(loc='upper left')
plt.show()
