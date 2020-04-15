# Let A be a 2D array whose entries are either W or B. 
# Write a program that takes A, and replaces all Ws that cannot reach the boundary with a B.

from collections import deque
def ComputeEnclosedRegions(board):
  queueStack = deque()
  for x in range(0, len(board)):
    for y in range(0, len(board[1])):
      if x == 0 or y == 0 or x == (len(board[1]) - 1) or y == (len(board) - 1):
        queueStack.append([x, y])
  while queueStack:
    coordin = queueStack.pop()
    x, y = coordin[0], coordin[1]
    if board[x][y] == "W":
      board[x][y] = "T"
      queueStack.extend(([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]))
  for x in range(0, len(board)):
    for y in range(0, len(board[1])):
      board[x][y] = "B" if board[x][y] != "T" else "W"
  return board


# arr = [[“W”, “B”,  “B”],
#        [“B”, “W”,  “B”],
#        [“W”, “B”,  “B”],
#        [“B”, “B”,  “B”]]
# print(ComputeEnclosedRegions(arr))