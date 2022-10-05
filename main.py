#Compounding

#store the inputs

# from numpy import number
# from pendulum import time


# principal = float(input('Enter the pricipal amount: '))
# rate = float(input('Enter the interest rate: '))
# time = float(input('Enter time in years: '))
# number = float(input('Enter the number of timer you want the interest to be compunded: '))


 
# #calculate total amount
# amount = principal * ((1 + ((rate/100)/number))** (number*time))

# #calculate compound interest

# ci = amount - principal 

# #display result

# print('Compound interest = %.2f' %ci)
# print('Total amount = %.2f' %amount)








# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show(block=False)
# input('press <ENTER> to continue')


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show(block=False)
# input('press <Enter> to continue')


# import statistics 
# print(statistics.stdev([1,3,5,7,8])) 


# import yfinance as yf
# stock_info = yf.Ticker('AAPL').info

# market_price = stock_info['regularMarketPrice']
# previous_close_price = stock_info['regularMarketPreviousClose']

# print('Apple market price', market_price)
# print('Apple previous close price', previous_close_price)



# import yfinance as yf
# import pendulum  
# import matplotlib.pyplot as plt

# price_history = yf.Ticker('AAPL').history(period='1y', interval='1d', actions=False) 
# time_series = list(price_history['Open'])
# dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]


# plt.style.use('dark_background')
# plt.plot(dt_list, time_series, linewidth=2)
# plt.show()



# #age
# birth_year=input("enter your brith year ")

# age = 2022 - int(birth_year)

# print(age)