'''
Q1: 


The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.
 

Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


'''


def treeDiameter(edges):
    # translate into adjacency list
    g = [set() for i in range(len(edges)+1)]
    for edge in edges:
        u, v = edge
        g[u].add(v)
        g[v].add(u)

    diameter = 0

    def dfs(curr, visited):
        nonlocal diameter

        maxDistance1 = maxDistance2 = currDist = 0
        visited[curr] = True

        # loop for each neighboring node in the graph
        for neighbor in g[curr]:

            # if we haven't visted a neighbor, visit and add to distance
            if not visited[neighbor]:
                currDist = 1 + dfs(neighbor, visited)

            # if the curr distance is the greatest we've encountered so far set maxDistance1 to curr distance
            if currDist > maxDistance1:
                maxDistance1, maxDistance2 = currDist, maxDistance1
            # otherwise if currdistance is smaller than our greatest distance but still larger than our second greatest distance, set maxDistance2 to curr distance
            elif currDist > maxDistance2:
                maxDistance2 = currDist

        # Diameter is equal to the sum of the two greatest distances
        diameter = max(diameter, maxDistance1 + maxDistance2)

        return maxDistance1

    visited = []
    for i in range(len(g)):
        visited.append(False)

    dfs(0, visited)

    return diameter


print(treeDiameter([[0, 1], [0, 2]]))
print(treeDiameter([[0, 1], [0, 2]]))
