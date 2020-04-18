# Design an efficient algorithm for computing the maximum total value for 
# the starting player in the pick-up-coins game.

# redo

# coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1,25 ,1 ,25, 5, 10]
# coins = [5, 25, 10, 1]
def coin_change(coins, amount):
  ways = [float("inf") for i in range(amount + 1)]
  ways[0] = 0
  for coin in coins:
    for current_amount in range(1, amount + 1):
      if coin <= current_amount:
        ways[current_amount] = min(ways[current_amount], 1 + ways[current_amount - coin])
              
  return ways[amount] if ways[amount] != float("inf") else -1