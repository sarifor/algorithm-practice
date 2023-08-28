# Backjoon 1753

import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())  # 노드 개수, 에지 개수
K = int(input())  # 출발 노드
distance = [sys.maxsize] * (V + 1)  # 거리 저장 리스트
visited = [False] * (V + 1)  # 방문 여부 저장 리스트
myList = [[] for _ in range(V + 1)]  # 에지 데이터 저장 인접 리스트
q = PriorityQueue()  # 다익스트라를 위한 우선순위 큐(우선순위가 높은 데이터가 먼저 나옴)

for _ in range(E):
  u, v, w = map(int, input().split())  # u에서 v로 가고, 가중치 w 부여
  myList[u].append((v, w))

q.put((0, K))  # K를 시작점으로 설정
distance[K] = 0

while q.qsize() > 0:
  current = q.get()
  c_v = current[1]  # 우선순위 큐에서 노드 가져오기
  if visited[c_v]:
    continue
  visited[c_v] = True

  for tmp in myList[c_v]:
    next = tmp[0]  # 연결 노드
    value = tmp[1]  # 가중치

    # 거리 리스트에서, '연결 노드의 값'이,
    # '시작 노드의 값과 시작 노드-연결 노드 간의 가중치의 합'보다 크다면,
    # 후자를 업데이트하고,
    # 우선순위 큐에 연결 노드 추가(정렬 기준: 거리 리스트의 '연결 노드의 값')
    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value
      q.put((distance[next], next))

for i in range(1, V + 1):
  if visited[i]:  # 각 노드를 방문한 적이 있다면, 해당 노드의 '거리 값' 출력
    print(distance[i])
  else:
    print("INF")
