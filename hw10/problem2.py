'''
Q2:
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph
'''

import collections


def getNumConnected(n, edges):
    # Adjacency list
    adjList = collections.defaultdict(list)
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)

    # dfs to find num connected
    res = 0
    seen = set()

    def dfs(i):
        seen.add(i)
        for j in adjList[i]:
            if j not in seen:
                dfs(j)
    for i in range(n):
        if i not in seen:
            dfs(i)
            res += 1
    return res


# testcases:
print(getNumConnected(5, [[0, 1], [1, 2], [3, 4]]))
print(getNumConnected(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
