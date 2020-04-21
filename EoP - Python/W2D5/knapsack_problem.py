# Write a program for the knapsack problem that selects a subset of items that has 
# maximum value and satisfies the weight constraint. All items have integer weights and values. 
# Return the value of the subset.

# class Clock:
#   def __init__(self, weight, value):
#     self.weight = weight
#     self.value = value


# # example input = [[$60, 5oz], [$50, 3oz]. [$70, 4oz], [$30, 2oz]] ==> ($80)  (3oz 20oz) given 5 oz constraint
# def knap_sack(clocks, weight_limit):
#     # outer for loop is the row    inner for loop is the col
#     tabBoard = [[0 for i in range(weight_limit + 1)]
#                 for i in range(len(clocks) + 1)]
#     # x represents the clock
#     for x in range(1, len(clocks)+1): 
#         # y represents the weight constraint
#         for y in range(1, weight_limit + 1):
#             clock = clocks[x - 1]
#             # print(clock.weight)
#             # print(x)
#             if clock.weight > y:
#                 tabBoard[x][y] = tabBoard[x - 1][y]
#             else:
#                 tabBoard[x][y] = max(
#                     tabBoard[x - 1][y], (clock.value + tabBoard[x - 1][y - clock.weight]))
#     return tabBoard[-1][-1]


# #            0, 1, 2,  3 ,  4 ,  5
# #          [0, 0, 0,   0,   0,   0]
# # $60/5 oz [0, 0, 0,   0,   0, $60]
# # $50/3 oz [0, 0, 0, $50, $50, $60] 
# # $70/4 oz [0, 0, 0, $50, $70, $70]
# # $30/2 oz [0, 0, 30, $50, $70,$80]



# attempt 2
# class Clock:
#   def __init__(self, weight, value):
#     self.weight = weight
#     self.value = value

# arr = [[60, 5], [50, 3], [70, 4], [30, 2]]
# arr2 = [[65, 20], [35, 8], [245, 60], [195, 55], [65, 40], [150, 70], [275, 85], [155, 25], [
#     120, 30], [320, 65], [75, 75], [40, 10], [200, 95], [100, 50], [220, 40], [99, 10]]
# clocks = []
# for ele in arr2:
#     clocks.append(Clock(ele[1], ele[0]))

# # print(clocks[0].weight)
# # print(clocks[0].value)

# print(knap_sack(clocks, 130))
# #Time complexity / space = o(m*n)



# [[$60, 5oz], [$50, 3oz]. [$70, 4oz], [$30, 2oz]]
# clocks = [
#       0, 1, 2, 3, 4, 5
#  none [0, 0, 0, 0, 0, 0],      
#  5oz [0, 0, 0, 0, 0, 60],
#  3oz [0, 0, 0, 50, 50, 60],
#  2oz [0, 0, 30, 50, 50, 80]]

# def knap_sack(clocks, weight):
#   dp = [[0 for j in range(weight + 1)] for i in range(len(clocks) + 1)]
#   for i in range(1, len(clocks) + 1):
#     for curr_weight in range(1, weight + 1):
#       clock = clocks[i - 1]
#       if clock.weight > curr_weight:
#         dp[i][curr_weight] = dp[i - 1][curr_weight]
#       elif clock.weight <= curr_weight:
#         dp[i][curr_weight] = max(dp[i - 1][curr_weight - clock.weight] + clock.value, dp[i-1][curr_weight])
#   return dp[-1][-1]

# print(knap_sack(clocks, 130))


