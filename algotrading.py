#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Using dual moving average crossover to determine when to buy and sell stock


# In[ ]:





# In[61]:


import pandas as pd
import numpy as np
from datetime import date,timedelta
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf


# In[62]:


google = yf.Ticker("GOOGL")
hist = google.history(period="max")
hist


# In[63]:


start_date = date.today() - timedelta(365)
start_date.strftime('%Y-%m-%d')

end_date = date.today() + timedelta(2)
end_date.strftime('%Y-%m-%d')


# In[64]:


def closing_price(ticker):
    asset = pd.DataFrame(yf.download(ticker,start=start_date,end=end_date)['Close'])
    return asset
google = closing_price('GOOGL')


# In[65]:


plt.plot(google)
plt.show()


# In[66]:


#Create the simple moving average with a 30 day window
SMA30 = pd.DataFrame(yf.download('GOOGL',start=start_date,end=end_date)['Close']).rolling(window = 30).mean()
SMA30
SMA100 = pd.DataFrame(yf.download('GOOGL', start=start_date, end = end_date)['Close']).rolling(window = 100).mean()
SMA100


# In[67]:


plt.plot(SMA30)
plt.plot(google)
plt.plot(SMA100)


# In[68]:


#When the short-term average crosses the long-term average => signal to buy
data = pd.DataFrame()
data['GOOGL'] = pd.DataFrame(yf.download('GOOGl', start=start_date, end=end_date)['Close'])
data['SMA30'] = pd.DataFrame(yf.download('GOOGL',start=start_date,end=end_date)['Close']).rolling(window = 30).mean()
data['SMA100'] = pd.DataFrame(yf.download('GOOGL', start=start_date, end = end_date)['Close']).rolling(window = 100).mean()
data


# In[69]:


#Create a function to signal when to buy and sell the stock
def transaction(data):
    sigPriceBuy = []
    sigPriceSell = []
    isFlagged = -1 #false
    
    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if isFlagged != 1:
                sigPriceBuy.append(data['GOOGL'][i])
                sigPriceSell.append(np.nan) #it's empty so don't add anything
                isFlagged = 1 #true
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
                if isFlagged != 0:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(data['GOOGL'][i])
                else:
                    sigPriceBuy.append(np.nan)
                    sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
       
        return (sigPriceBuy, sigPriceSell) 
                


# In[71]:


data['Buy_Signal_Price'] = pd.DataFrame(transaction[0])
data['Sell_Signal_price'] = pd.DataFrame(transaction[1])
data


# In[ ]:


#Visualize data and strategy


# In[ ]:




