from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive DFS traversal function that finds
    # all reachable vertices for s
    def DFSUtil(self, s, v):

        # Mark reachability from s to v as true.
        if (s == v):
            if (v in self.graph[s]):
                self.tc[s][v] = 1
        else:
            self.tc[s][v] = 1

        # Find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                if s == i:
                    self.tc[s][i] = 1
                else:
                    self.DFSUtil(s, i)

    # The function to find transitive closure. It uses
    # recursive DFSUtil()
    def transitiveClosure(self):

        # Call the recursive helper function to print DFS
        # traversal starting from all vertices one by one
        for i in range(self.V):
            self.DFSUtil(i, i)

        print(self.tc)


def transitive_closure():
    g = Graph(16)

    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(0, 12)
    g.addEdge(0, 8)
    g.addEdge(0, 6)
    g.addEdge(1, 2)
    g.addEdge(1, 13)
    g.addEdge(1, 0)
    g.addEdge(1, 11)
    g.addEdge(1, 8)
    g.addEdge(1, 6)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 6)
    g.addEdge(3, 13)
    g.addEdge(3, 12)
    g.addEdge(3, 8)
    g.addEdge(3, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 2)
    g.addEdge(5, 9)
    g.addEdge(5, 14)
    g.addEdge(6, 1)
    g.addEdge(6, 0)
    g.addEdge(6, 3)
    g.addEdge(6, 11)
    g.addEdge(7, 12)
    g.addEdge(8, 6)
    g.addEdge(8, 1)
    g.addEdge(8, 0)
    g.addEdge(8, 3)
    g.addEdge(8, 11)
    g.addEdge(8, 12)
    g.addEdge(9, 12)
    g.addEdge(9, 14)
    g.addEdge(9, 15)
    g.addEdge(10, 4)
    g.addEdge(10, 13)
    g.addEdge(11, 8)
    g.addEdge(11, 6)
    g.addEdge(11, 1)
    g.addEdge(11, 0)
    g.addEdge(11, 13)
    g.addEdge(12, 15)
    g.addEdge(12, 7)
    g.addEdge(12, 11)
    g.addEdge(12, 3)
    g.addEdge(13, 10)
    g.addEdge(13, 2)
    g.addEdge(13, 12)
    g.addEdge(14, 9)
    g.addEdge(15, 12)
    g.addEdge(15, 14)
    g.addEdge(15, 5)
    g.addEdge(15, 9)

    g.transitiveClosure()
