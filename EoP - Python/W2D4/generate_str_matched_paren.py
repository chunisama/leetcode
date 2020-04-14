# Strings in which parens are matched are defined by the following three rules:
# o The empty string, "" , is a string in which parens are matched.
# o The addition of a leading left parens and a trailing right parens to a string in which parens
# are matched results in a string in which parens are matched. For example, since "(0)0" is a
# string with matched parens, so is "((0)0)".
# o The concatenation of two strings in which parens are matched is itself a string in which
# Parens are matched. For example, since "(0)0" Ntd "0" are strings with matched parens, so
# is "(0X)0".
# For example, the set of strings containing two pairs of matched parens is t(0) 00), a.rd the set
# of strings with three pairs of matched parens is {((0)), (00), (0)0,0(0),000}.
# Write a program that takes as input a number and returns all the strings with that number of matched pairs of parens.

# redo