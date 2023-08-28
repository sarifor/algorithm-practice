# Backjoon 1854

import sys
import heapq
input = sys.stdin.readline
N, M, K = map(int, input().split()) # 노드 개수, 에지 개수, K번째
W = [[] for _ in range(N+1)] # 인접 리스트
distance = [[sys.maxsize] * K for _ in range(N+1)] # 거리 리스트

for _ in range(M): 
    a, b, c = map(int, input().split()) # a에서 b로 가고, 가중치 c 부여
    W[a].append((b, c)) # 인접 리스트에 에지 정보 저장

pq = [(0, 1)] # 우선순위 큐(heapq)에 '시작 도시의 최단 거리'와 '시작 도시' 저장
distance[1][0] = 0 # 시작 도시의 최단 거리 저장

while pq:
    cost, node = heapq.heappop(pq) # 거리 값이 제일 적은 노드가 선택됨
    for nNode, nCost in W[node]: # 현재 노드의 연결 노드와 가중치를 꺼내서
        sCost = cost + nCost # 새로운 총 거리를 구하고
        if distance[nNode][K-1] > sCost: # 연결 노드의 K번째 경로와 신규 경로 비교
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode]) # 우선순위 큐에 새로운 데이터(거리, 노드) 추가

for i in range(1, N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])