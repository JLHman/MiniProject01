# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project 1


import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt




# rok = yf.Ticker("ROK")

# get stock info
# rok.info

# get historical market data
# hist = rok.history(period="max")

data = yf.download("ROK", start="2022-09-01", end="2022-09-16")
# print(data)

rokPrices = []

for price in data['Adj Close']:
    rokPrices.append(price)

print(rokPrices)

# Create a numpy array
rokarray = np.array(rokPrices)
# Create a Graph with matplotlib and label y axis
plt.plot(rokarray)
plt.ylabel('Stock Price')
# Show Graph
plt.show()



