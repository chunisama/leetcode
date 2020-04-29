# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 
# iterative solution: O(n)
def cloneGraph(self, node: 'Node') -> 'Node':
    # adjlist = [[2,4], [1,3], [2, 4], [1,3]]
    if not node:
        return
    cloned_node = Node(node.val,[])
    visited = {node: cloned_node}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in visited:
                cloned_neighbor = Node(neighbor.val, [])
                visited[neighbor] = cloned_neighbor
                visited[node].neighbors.append(cloned_neighbor)
                stack.append(neighbor)
            else:
                visited[node].neighbors.append(visited[neighbor])
    return cloned_node
        