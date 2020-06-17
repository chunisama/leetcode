# Design a raffle system that has the functionality to addPlayer(email), removePlayer(email), and pickWinner(), 
# all in constant time.

import random
class raffleSystem(object):

  def __init__(self):
    # self.tickets = set()
    self.tickets = {}

  def addPlayer(self, email):
    # self.tickets.add(email)
    if email in self.tickets:
      self.tickets[email] += 1
    else:
      self.tickets[email] = 1

  def removePlayer(self, email):
    # self.tickets.remove(email)
    del self.tickets[email]
    
  def pickWinner(self): 
    temp = []
    for email in self.tickets:
      k = 0
      while k <= self.tickets[email]:
        temp.append(email)
        k += 1
    random_idx = random.randint(0, len(temp))
    return temp[random_idx]
