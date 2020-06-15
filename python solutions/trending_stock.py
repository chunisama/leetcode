# implement trendingStock() a class simulates and outputs the most frequently traded stock

# 1) processStock(stringStock) processes the stock into the system
# 2) getTrendingStock() removes and returns the most frequent traded stock in the system
# if there is a tie for most traded stock the stock most recently traded is removed and returned


# ex) test = trendingStock()
# test.processStock('TSLA')
# test.processStock('APPL')
# test.processStock('TLSA') => DISPLAY TLSA THEN DECREMENT THE COUNT
# test.processStock('APPL) => most recently traded stock and remove it
# test.processStock('NTFX)  
# test.processStock('NTFX) => tsla traded three times remove tsla from the system



class trendingStock(object):
  def __init__(self):
    self.storage = {}
    self.max = 0
  
  def processStock(self, stock):
    if stock in self.storage:
      self.storage[stock] += 1
    else:
      self.storage[stock] = 1
    self.max = max(self.max, self.storage[stock])
  def getTrendingStock(self):
    stocks = list(self.storage.keys())
    trendingStock = None
    for i in range(len(stocks) - 1, -1, -1):
      if self.storage[stocks[i]] == self.max:
        del self.storage[stocks[i]]
        if self.max - 1 > 0:
          self.storage[stocks[i]] = self.max - 1
        trendingStock = stocks[i]
        break
    values = list(self.storage.values())
    self.max = max(values)
    return (trendingStock, self.storage[trendingStock], self.storage)
    


      
test = trendingStock()
print(test.processStock('TSLA'))
print(test.processStock('APPL'))
print(test.processStock('TSLA'))
print(test.getTrendingStock())
print(test.processStock('APPL')) 
print(test.getTrendingStock())
print(test.processStock('NTFX'))  
print(test.processStock('TSLA'))
print(test.getTrendingStock())