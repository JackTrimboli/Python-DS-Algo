class Graph:
    def __init__(self):
        self.V = set()
        self.adj = {}


def BFS(G, s):
    for u in G.V:
        u.color = 'WHITE'
        u.d = float('inf')
        u.p = None
    s.color = 'GRAY'
    s.d = 0
    s.p = None

    Q = []
    Q.append(s)

    while len(Q) != 0:
        u = Q.pop(0)
        for v in G.adj[u]:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.d = u.d + 1
                v.p = u
                Q.append(v)
        u.color = "BLACK"


def DFS(G, s):
    # iterate over vertices
    for u in G.V:
        u.color = 'WHITE'
        u.d = float('inf')
        u.p = None

    s.color = 'GRAY'
    s.d = 0
    s.p = None

    Q = []
    Q.append(s)

    while len(Q) != 0:
        u = Q.pop()
        for v in G.adj[u]:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.d = u.d + 1
                v.p = u
                Q.append(v)
        u.color = "BLACK"


def dfsbymem(G, s):
    # for each vertice, we want to mark it as unvisited
    for u in G.V:
        u.color = 'WHITE'
        u.d = float('inf')
        u.p = None

    # Create a stack
    S = []
    s.color = 'GRAY'
    s.d = 0
    s.p = None

    # push S onto stack
    S.append(s)

    while len(S) > 0:
        u = S.pop()
        for v in G.adj[u]:
            print(v)
            v.color = 'GRAY'
            v.d = u.d + 1
            v.p = u
            S.append(v)
        u.color = 'BLACK'


G = Graph()
