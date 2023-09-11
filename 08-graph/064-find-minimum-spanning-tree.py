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
N, M = map(int, input().split())  # 노드 수, 에지 수
pq = PriorityQueue()  # 우선순위 큐
parent = [0] * (N + 1)  # 대표 노드 저장 리스트

# 대표 노드 저장 리스트 초기화
for i in range(N + 1):
  parent[i] = i

# 우선순위 큐에 에지 정보 저장
for i in range(M):
  s, e, w = map(int, input().split())
  pq.put((w, s, e))  # 우선순위 큐이므로 자동 정렬


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


useEdge = 0  # 사용 에지 수
result = 0  # 정답

# 사용한 에지 수가 '노드 수 -1'이 될 때까지
while useEdge < N - 1:
  w, s, e = pq.get()
  # 에지 시작점과 끝점의 부모 노드가 다르면
  if find(s) != find(e):
    union(s, e)  # 연결하고
    result += w  # 에지 가중치를 정답에 더하고
    useEdge += 1  # 사용 에지 수 1 증가

# 정답 출력
print(result)
