# Backjoon 11404
# If k is an intermediate vertex in shortest path from i to j,
# and dist[i][j] > dist[i][k] + dist[k][j],
# update the value of dist[i][j] as dist[i][k] + dist[k][j].

import sys

input = sys.stdin.readline
N = int(input())  # 도시 개수
M = int(input())  # 노선 개수
distance = [[sys.maxsize for j in range(N + 1)] for i in range(N + 1)]  # 인접 행렬

# 시작 도시와 종료 도시가 같은 자리에 0 저장
for i in range(1, N + 1):
  distance[i][i] = 0

# 노선 데이터를 인접 행렬에 저장
for i in range(M):
  s, e, v = map(int, input().split())
  if distance[s][e] > v:
    distance[s][e] = v

# 전체 경로의 최단 경로가 부분 경로의 최단 경로의 조합보다 클 경우, 후자로 업데이트
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      if distance[i][j] > distance[i][k] + distance[k][j]:
        distance[i][j] = distance[i][k] + distance[k][j]

# 정답 출력
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if distance[i][j] == sys.maxsize:
      print(0, end=' ')
    else:
      print(distance[i][j], end=' ')
  print()