import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import yfinance as yf
from IPython.core.pylabtools import figsize

msft = yf.Ticker('MSFT')

print(msft.info)

hist = msft.history(period = "max")
print(hist)
hist.plot(figsize(12,12),kind="line",subplots=True)
plt.show()

# print(msft.actions) #dividents or stock splits

# print(msft.dividends)

# print(msft.splits)

# print(msft.quarterly_financials)

# print(msft.major_holders)

# print(msft.institutional_holders)

# print(msft.cashflow)

# print(msft.sustainability) # not working 09062023

# print(msft.recommendations) # not working 09062023

# print(msft.calendar) # not working 09062023

# print(msft.options)

