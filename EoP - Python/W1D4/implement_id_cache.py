# Create a cache for looking up prices of books identified by their ISBN. 
# You implement lookup, insert, and remove methods. 
# Use the Least Recently Used (LRU) policy for cache eviction. If an ISBN is already present, 
# insert should not change the price, but it should update that entry tobe the most recently 
# used entry. Lookup should also update that entry to be the most recently used entry.

# implement a cache class
# methods: insert, remove, lookup
import collections
class IdCache:
  def __init__(self, capacity):
    self.price_table = collections.OrderedDict()
    self.capacity = capacity

  def insert(self, id, price):
    if len(self.price_table) == self.capacity:
      if id in self.price_table:
        self.price_table.pop(id)
        self.price_table[id] = price
      else:
        self.price_table.pop()
        self.price_table[id] = price
    else:
      if id in self.price_table:
        self.price_table.pop(id)
        self.price_table[id] = price
      else: 
        self.price_table[id] = price

  def remove(self, id):
    self.price_table.pop(id)

  def lookup(self, id):
    price = self.price_table.pop(id)
    self.price_table[id] = price
    return price




