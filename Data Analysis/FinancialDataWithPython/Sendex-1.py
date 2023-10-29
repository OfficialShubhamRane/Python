import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf

yf.pdr_override()
import pandas as pd
import pandas_datareader.data as pdr

style.use('ggplot')

df = pdr.get_data_yahoo('TSLA', start='2000-1-1')
print(df.columns)
# df.to_csv('E:\Python\Data Analysis\FinancialDataWithPython\Resources\Outputs\Tesla.csv')

df[['Adj Close','Open']].tail(60).plot()
plt.show()