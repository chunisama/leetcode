# Given a 2d board as an arg, check the 2d board to ensure no duplicate numbers 
# within row, col
# check the 3x3 quadrants as well

# use a nested loop to check if row has duplicates, col has duplicates
# initialize a new set to check for duplicity for each col and row
# return false if duplicity exists return true after nested loop

import numpy
def sudoku_checker(board):
  # checking numbers in each row
  for row in board:
    dup_check = set(row)
    if len(dup_check) != len(row):
      return False
  # checking numbers in each column
  tranposed_board = numpy.tranpose(board)
  for col in tranposed_board:
    dup_check = set(col)
    if len(dup_check) != len(col):
      return False
  # checking in 3x3 quadrant
  for row in (0, 3, 6):
    for col in (0, 3, 6):
      quadrant = [board[x][y] for x in range(row, row + 3) for y in range(col, col + 3)]
      dup_check = set(quadrant)
      if len(dup_check) != len(quadrant):
        return False
  return True






