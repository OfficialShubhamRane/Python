import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import yfinance as yf
from IPython.core.pylabtools import figsize

major_indices = pd.read_html("https://finance.yahoo.com/world-indices")[0]
ticker_list = major_indices["Symbol"].str.replace("^","").str.lower().to_list()
print(ticker_list)

# ticker_data = yf.Tickers(ticker_list)
# print(ticker_data)

df = yf.download(ticker_list, period='1d', start="2020-01-13", end="2023-07-09")
adj_close = df.dropna(thresh=10, axis=1)['Adj Close']
print(adj_close.head().describe().T)

adj_close.plot(figsize(16,8),subplots=True)
plt.show()

