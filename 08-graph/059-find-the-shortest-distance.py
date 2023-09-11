# Backjoon 11657
# |V| is the number of vertices in given graph.
# Do follwoing |V|-1 times for edge u-v:
# If dist[v] > dist[u] + weight of edge uv,
# then dist[v] = dist[u] + weight of edge uv.
# Again traverse every edge and do following for each edge u-v:
# If dist[v] > dist[u] + weight of edge uv, then 'Graph contains negative weight cycle'

import sys

input = sys.stdin.readline
N, M = map(int, input().split())  # 노드 개수, 에지 개수
edges = []  # 에지 리스트
distance = [sys.maxsize] * (N + 1)  # 거리 리스트

for i in range(M):  # 언더바(_) 사용이 바람직
  start, end, time = map(int, input().split())
  edges.append((start, end, time))  # 에지 리스트에 에지 정보 저장

distance[1] = 0

# '노드 개수 -1'만큼 라운드 반복
for _ in range(N - 1):
  # 매 반복마다 '모든 간선'을 확인하며
  for start, end, time in edges:
    # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 리스트 업데이트
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
      distance[end] = distance[start] + time

mCycle = False

# 라운드 한 번 더 반복
for start, end, time in edges:
  # 값이 갱신된다면
  if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
    # 음수 사이클 존재
    mCycle = True

# 음수 사이클 미존재 -> 거리 리스트 출력
if not mCycle:
  for i in range(2, N + 1):
    if distance[i] != sys.maxsize:
      print(distance[i])
    # 단, 거리 리스트의 값이 무한대일 때 -1 출력
    else:
      print(-1)
# 음수 사이클 존재 -> -1 출력
else:
  print(-1)
