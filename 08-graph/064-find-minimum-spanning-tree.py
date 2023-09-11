# Backjoon 1197
# Minimum Spanning Tree(MST) using Kruskal's algorithm:
# 1. Sort all the edges in ascending order of their weight.
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
# If the cycle is not formed, include this edge. Else, discard it.
# Step 2 uses the Union-Find algorithm to detect cycles.
# 3. If the number of nodes is V, the number of edges to be taken is equal to V-1.
# Repeat step 2 until there are V-1 edges in the spanning tree.

import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)

for i in range(N + 1):
  parent[i] = i

for i in range(M):
  s, e, w = map(int, input().split())
  pq.put((w, s, e))


def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a


useEdge = 0
result = 0

while useEdge < N - 1:
  w, s, e = pq.get()
  if find(s) != find(e):
    union(s, e)
    result += w
    useEdge += 1

print(result)