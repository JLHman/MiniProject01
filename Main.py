# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project 1

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# get data for Rockwell stock from yfinance api
data = yf.download("ROK", start="2022-09-01", end="2022-09-16")
# print(data)

rokPrices = []

# Get the closing price from the data output
for price in data['Adj Close']:
    rokPrices.append(price)

print(rokPrices)

# Create a numpy array
rokarray = np.array(rokPrices)
# Create a Graph with matplotlib and label y axis
plt.plot(rokarray)
plt.ylabel('Stock Price')
plt.xlabel('Days')

# Save Graph
plt.savefig('charts/rok.png')

# Show Graph
plt.show()

# get data for Cisco stock from yfinance api
data = yf.download("CSCO", start="2022-09-01", end="2022-09-16")
# print(data)

cscoPrices = []

# Get the closing price from the data output
for price in data['Adj Close']:
    cscoPrices.append(price)

print(cscoPrices)

# Create a numpy array
cscoarray = np.array(cscoPrices)
# Create a Graph with matplotlib and label y axis
plt.plot(cscoarray)
plt.ylabel('Stock Price')
plt.xlabel('Days')

# Save Graph
plt.savefig('charts/csco.png')

# Show Graph
plt.show()

# get data for ABB stock from yfinance api
data = yf.download("ABB", start="2022-09-01", end="2022-09-16")
# print(data)

abbPrices = []

# Get the closing price from the data output
for price in data['Adj Close']:
    abbPrices.append(price)

print(abbPrices)

# Create a numpy array
abbarray = np.array(abbPrices)
# Create a Graph with matplotlib and label y axis
plt.plot(abbarray)
plt.ylabel('Stock Price')
plt.xlabel('Days')

# Save Graph
plt.savefig('charts/abb.png')

# Show Graph
plt.show()

# get data for GE stock from yfinance api
data = yf.download("GE", start="2022-09-01", end="2022-09-16")
# print(data)

gePrices = []

# Get the closing price from the data output
for price in data['Adj Close']:
    gePrices.append(price)

print(gePrices)

# Create a numpy array
gearray = np.array(gePrices)
# Create a Graph with matplotlib and label y axis
plt.plot(gearray)
plt.ylabel('Stock Price')
plt.xlabel('Days')

# Save Graph
plt.savefig('charts/ge.png')

# Show Graph
plt.show()

# get data for Schneider Electric stock from yfinance api
data = yf.download("SBGSY", start="2022-09-01", end="2022-09-16")
# print(data)

sbgsyPrices = []

# Get the closing price from the data output
for price in data['Adj Close']:
    sbgsyPrices.append(price)

print(sbgsyPrices)

# Create a numpy array
sbgsyarray = np.array(sbgsyPrices)
# Create a Graph with matplotlib and label y axis
plt.plot(sbgsyarray)
plt.ylabel('Stock Price')
plt.xlabel('Days')

# Save Graph
plt.savefig('charts/sbgsy.png')

# Show Graph
plt.show()

