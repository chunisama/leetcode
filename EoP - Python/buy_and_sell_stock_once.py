# Consider the following sequence of stock prices: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# The maximum profit that can be made with one buy and one sell is 30 - buy at 260 and sell at 290

# Write a program that takes an array denoting the daily stock price and retursn the max profit
# that could be made by buying and then selling one share of that stock. no need to buy if no profit is possible

def buy_and_sell_stock_once(prices)
  min_price, max_profit = float('inf'), 0.0
  for price in prices:
    max_profit_sell_today = price - min_price
    max_profit = max(max_profit, max_profit_sell_today)
    min_price = min(min_price, price)
  return max_profit
  