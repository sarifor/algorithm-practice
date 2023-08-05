# Backjoon 1260 (DFS omitted)
# DFS proceeds through the nodes as far as possible until reaching the node with no unvisited nearby node,
# while BFS walks through all nodes on the same level before moving on to the next level.

from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N + 1)
BFS(Start)