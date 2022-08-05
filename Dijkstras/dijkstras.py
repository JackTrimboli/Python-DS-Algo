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


def dijkstras(G, w, s):
    return
