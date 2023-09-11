# Backjoon 11657
# |V| is the number of vertices in given graph.
# Do follwoing |V|-1 times for edge u-v:
# If dist[v] > dist[u] + weight of edge uv,
# then dist[v] = dist[u] + weight of edge uv.
# Again traverse every edge and do following for each edge u-v:
# If dist[v] > dist[u] + weight of edge uv, then 'Graph contains negative weight cycle'

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1)

for i in range(M):  # Use _ is recommended
  start, end, time = map(int, input().split())
  edges.append((start, end, time))

distance[1] = 0

for _ in range(N - 1):
  for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      distance[end] = distance[start] + time

mCycle = False

for start, end, time in edges:
  if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
    mCycle = True

if not mCycle:
  for i in range(2, N + 1):
    if distance[i] != sys.maxsize:
      print(distance[i])
    else:
      print(-1)
else:
  print(-1)