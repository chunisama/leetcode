# Write a program that takes a final score and scores for individual plays, and 
# returns the number of combinations of plays that result in the final score.

def count_number_score_combinations(num_plays, total_score):
  dp = [[0 for i in range(total_score + 1)] for i in range(len(num_plays))]
  
  for i in range(len(num_plays)):
    for j in range(total_score + 1):
      play = num_plays[i]
      if j == play:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i - 1][j] + dp[i][j - num_plays[i]]
  return dp[-1][-1]


# redo
print(count_number_score_combinations([2,3,7], 12))