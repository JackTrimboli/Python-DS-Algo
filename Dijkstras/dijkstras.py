'''
def DIJKSTRAS(G,w,s):
    for each vertex v in G.V
        v.d = inf
        v.pi = NIL
    s.d = 0 
    S = empty
    Q = G.V
    while Q != empty
        u = EXTRACT-MIN(Q)
        S = S OR {u}
        for each vertex v in G.adj[u]
            if v.d > u.d + w(u,v) #relaxing an edge (should i update?)
                v.d = u.d + w(u,v)
                v.pi = u
                DECREASE-KEY(Q,v,v.d)
'''
import heapq


def dijkstras(G, w, s):
    return
    # for v in G.V:
    #     v.d = float('int')
    #     v.pi = NONE
    # s.d = 0
    # seen = set()
    # Q = heapq.heapify(G.V)

    # while len(Q) > 0:
    #     u = heapq.heappop(Q)

    #     if seen[u]: continue

    #     seen[u] = True


'''
- Create a set "seen" to keep track of visited nodes

- Create a dict "parentsMap" for parents map to reconstruct the path after execution of algo

- Create a dict nodeCosts for keeping track of min cost 
'''
