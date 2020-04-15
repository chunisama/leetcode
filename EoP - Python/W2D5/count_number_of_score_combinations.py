# Write a program that takes a final score and scores for individual plays, and 
# returns the number of combinations of plays that result in the final score.

def count_number_score_combinations(scores, final_score):
  dp = [[[]]] + [[] for _ in range(final_score)]
  for score in scores:
    for i in range(score, final_score + 1):
      dp[i] += [sublist + [score] for sublist in dp[i - score]]
  return dp[final_score]
  
# redo

print(count_number_score_combinations([2,3,7], 12))