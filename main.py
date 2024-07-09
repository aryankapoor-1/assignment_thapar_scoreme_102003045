
### 2. `main.py`

# python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    def topological_sort(graph):
        n = len(graph)
        in_degree = [0] * n
        for i in range(n):
            for j, w in graph[i]:
                in_degree[j] += 1

        stack = [i for i in range(n) if in_degree[i] == 0]
        topo_order = []

        while stack:
            node = stack.pop()
            topo_order.append(node)
            for neighbor, weight in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        return topo_order

    def calculate_longest_path(graph, topo_order):
        n = len(graph)
        dist = [-float('inf')] * n
        
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight

        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)
