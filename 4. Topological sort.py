from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list
        self.V = vertices  # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add edge from u to v

    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store topological sort
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Return the contents of the stack in reverse order
        return stack[::-1]

# Example usage:
g = Graph(6)  # Create a graph with 6 vertices
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
print(g.topological_sort())


output:

Topological Sort:
[5, 4, 2, 3, 1, 0]
