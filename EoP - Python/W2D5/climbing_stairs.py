# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbing_stairs(n):
  if n == 1: return 1
  table = [1, 2]
  for num in range(2, n):
    table.append(table[num - 1] + table[num - 2])
  return table[-1]