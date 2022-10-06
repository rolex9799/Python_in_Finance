#show current stock price

import yfinance as yf
stock_info = yf.Ticker('AAPL').info

market_price = stock_info['regularMarketPrice']
previous_close_price = stock_info['regularMarketPreviousClose']

print('Apple market price', market_price)
print('Apple previous close price', previous_close_price)



# show historical stock data
# import yfinance as yf
# import pendulum  
# import matplotlib.pyplot as plt

# price_history = yf.Ticker('AAPL').history(period='1y', interval='1d', actions=False) 
# time_series = list(price_history['Open'])
# dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]


# plt.style.use('dark_background')
# plt.plot(dt_list, time_series, linewidth=2)
# plt.show()

