class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def DFS(graph, C, root, descendant):
    for child in graph.adjList[descendant]:
        if C[root][child] == 0:
            C[root][child] = 1
            DFS(graph, C, root, child)


def confereAlcance():
    edges = [(0, 2), (0, 3), (0, 12), (0, 8), (0, 6),
             (1, 2), (1, 13), (1, 0), (1, 11), (1, 8), (1, 6),
             (2, 4), (2, 3), (2, 0), (2, 6),
             (3, 13), (3, 12), (3, 8), (3, 0),
             (4, 0), (4, 2),
             (5, 9), (5, 14),
             (6, 1), (6, 0), (6, 3), (6, 11),
             (7, 12),
             (8, 6), (8, 1), (8, 0), (8, 3), (8, 11), (8, 12),
             (9, 12), (9, 14), (9, 15),
             (10, 4), (10, 13),
             (11, 8), (11, 6), (11, 1), (11, 0), (11, 13),
             (12, 15), (12, 7), (12, 11), (12, 3),
             (13, 10), (13, 2), (13, 12),
             (14, 9),
             (15, 12), (15, 14), (15, 5), (15, 9)
             ]
    n = 16

    graph = Graph(edges, n)

    C = [[0 for x in range(n)] for y in range(n)]

    for v in range(n):
        C[v][v] = 1
        DFS(graph, C, v, v)
        print(C[v])
