# Consider a vertex type for a directed graph in which there are two fields: an integer label and a list of references 
# to other vertices. Design an algorithm that takes a reference to a vertex u, arrd creates a copy of the graph on the 
# vertices reachable from z. Return the copy of u.

# review and redo

def clone_graph(node):
  stack = [node]
  graph = {}
  while len(stack):
    new_node = stack.pop()
    for edge in node.edges:
      if edge not in graph:
        graph[edge] = edge.label
        stack.append(edge)
      graph[new_node].edges.append(graph[edge])
  return graph


def cloneGraph(self, node: 'Node') -> 'Node':
  dic = {}
  def dfs(node):
    if not node:
      return
    else:
      node_copy = Node(node.val, [])
      dic[node] = node_copy
      for nei in node.neighbors:
        if nei in dic:
          node_copy.neighbors.append(dic[nei])
        else:   
          node_copy.neighbors.append(dfs(nei))
    return node_copy
  return dfs(node)

