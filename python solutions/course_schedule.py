# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses-1.

# Some courses may have prerequisites, 
# for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs,
#  is it possible for you to finish all courses?

 
# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.

def canFinish(numCourses, prerequisites):
  graph = {key: [] for key in range(numCourses)}
  for pair in prerequisites:
    graph[pair[0]].append(pair[1])
  visited = set()
  completed = set()
  def dfs(key):
    if key in visited: return
    visited.add(key)
    if not graph[key]:
      completed.add(key)
      return
    else:
      for pre in graph[key]:
        if pre not in visited:
          dfs(pre)
        elif pre not in completed:
          return
      completed.add(key)
  for course in graph:
    dfs(course)
  return len(completed) == len(visited)