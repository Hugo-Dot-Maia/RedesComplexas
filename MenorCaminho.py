# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :O(V+E)
from collections import defaultdict


# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge
class Graph:
    def __init__(self, vertices):

        self.V = vertices  # No. of vertices

        # dictionary containing adjacency List
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    # A recursive function used by shortestPath
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)

        # Push current vertex to stack which stores topological sort
        stack.append(v)

    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''

    def shortestPath(self, s):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from source vertices
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)

        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        # Process vertices in topological order
        while stack:

            # Get the next vertex from topological order
            i = stack.pop()

            # Update distances of all adjacent vertices
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        # Print the calculated shortest distances
        retorno = []
        for i in range(self.V):
            retorno.append(dist[i])
            print(("%d" % dist[i]) if dist[i] != float("Inf") else "Inf", end=" ")

        return retorno


def menorCaminho(s):
    g = Graph(16)

    g.addEdge(0, 2, 1)
    g.addEdge(0, 3, 1)
    g.addEdge(0, 12, 1)
    g.addEdge(0, 8, 1)
    g.addEdge(0, 6, 1)
    g.addEdge(1, 2, 1)
    g.addEdge(1, 13, 1)
    g.addEdge(1, 0, 1)
    g.addEdge(1, 11, 1)
    g.addEdge(1, 8, 1)
    g.addEdge(1, 6, 1)
    g.addEdge(2, 4, 1)
    g.addEdge(2, 3, 1)
    g.addEdge(2, 0, 1)
    g.addEdge(2, 6, 1)
    g.addEdge(3, 13, 1)
    g.addEdge(3, 12, 1)
    g.addEdge(3, 8, 1)
    g.addEdge(3, 0, 1)
    g.addEdge(4, 0, 1)
    g.addEdge(4, 2, 1)
    g.addEdge(5, 9, 1)
    g.addEdge(5, 14, 1)
    g.addEdge(6, 1, 1)
    g.addEdge(6, 0, 1)
    g.addEdge(6, 3, 1)
    g.addEdge(6, 11, 1)
    g.addEdge(7, 12, 1)
    g.addEdge(8, 6, 1)
    g.addEdge(8, 1, 1)
    g.addEdge(8, 0, 1)
    g.addEdge(8, 3, 1)
    g.addEdge(8, 11, 1)
    g.addEdge(8, 12, 1)
    g.addEdge(9, 12, 1)
    g.addEdge(9, 14, 1)
    g.addEdge(9, 15, 1)
    g.addEdge(10, 4, 1)
    g.addEdge(10, 13, 1)
    g.addEdge(11, 8, 1)
    g.addEdge(11, 6, 1)
    g.addEdge(11, 1, 1)
    g.addEdge(11, 0, 1)
    g.addEdge(11, 13, 1)
    g.addEdge(12, 15, 1)
    g.addEdge(12, 7, 1)
    g.addEdge(12, 11, 1)
    g.addEdge(12, 3, 1)
    g.addEdge(13, 10, 1)
    g.addEdge(13, 2, 1)
    g.addEdge(13, 12, 1)
    g.addEdge(14, 9, 1)
    g.addEdge(15, 12, 1)
    g.addEdge(15, 14, 1)
    g.addEdge(15, 5, 1)
    g.addEdge(15, 9, 1)

    print("Following are shortest distances from source %d " % s)
    return g.shortestPath(s)
