# Design an algorithm that takes as input two teams and the heights of the players in the teams and checks 
# if it is possible to place players to take the photo subject to the placement constraint.

# assuming team lengths are the same
def team_photo_day(team_a, team_b):
  sorted_a = sorted(team_a)
  sorted_b = sorted(team_b)
  for idx in range(team_a):
    if sorted_a[idx] > sorted_b[idx]:
      return False
  return True


