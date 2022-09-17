# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


#rok = yf.Ticker("ROK")

# get stock info
#rok.info

# get historical market data
#hist = rok.history(period="max")

#tickers = yf.Tickers('rok csco abb sbgsy ge')

data = yf.download("ROK", start="2022-09-01", end="2022-09-16")
#print(data)

rokPrices = []

for price in data['Adj Close']:
    rokPrices.append(price)

print(rokPrices)

# Create a numpy array
rokarray = np.array([rokPrices])


