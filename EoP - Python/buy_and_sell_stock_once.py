# Consider the following sequence of stock prices: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# The maximum profit that can be made with one buy and one sell is 30 - buy at 260 and sell at 290

# Write a program that takes an array denoting the daily stock price and retursn the max profit
# that could be made by buying and then selling one share of that stock. no need to buy if no profit is possible

# def buy_and_sell_stock_once(prices):
#   min_price, max_profit = float('inf'), 0.0
#   for price in prices:
#     max_profit_sell_today = price - min_price
#     max_profit = max(max_profit, max_profit_sell_today)
#     min_price = min(min_price, price)
#   return max_profit

prices = [310, 315, 275, 295, 260, 270, 290, 255, 250] # => 30
# Initilize two variables min, max = 0, infinity
# Answer => max profit = max - min
# Iterate thru my list prices and compare each price to my min and max
# Return max profit

import math
def buy_and_sell_stock_once(prices):
  current_min, current_max = math.inf, 0 
  max_profit = 0
  for price in prices:
    current_min = min(current_min, price)
    current_max = max(current_max, price - current_min)
    max_profit = max(current_max, max_profit)
  return max_profit
  
print(buy_and_sell_stock_once(prices))