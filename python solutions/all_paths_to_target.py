# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # adj_list = {
        #     0 : [1, 2],
        #     1 : [3],
        #     2 : [3]
        #     3 : []
        # }
        adj_list = {}
        paths = []
        # populate adj list
        for idx, sub_arr in enumerate(graph):
            adj_list[idx] = sub_arr
        # dfs to check all 
        def dfs(node, path, graph):
            if node == len(graph) - 1:
                path = path + [node]
                paths.append(path)
                return
            for neigh in adj_list[node]:
                dfs(neigh, path + [node], graph)
        dfs(0,[], graph)
        return paths