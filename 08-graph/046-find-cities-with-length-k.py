# Backjoon 18352

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 노드 수, 에지 수, 목표 거리, 시작점
A = [[] for _ in range(N + 1)] # 인접 리스트
answer = []
visited = [-1] * (N + 1) # 방문 리스트

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1 # 최초 노드는 거리 0
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1: # 현재 노드의 연결 노드 중 방문하지 않은 노드가 있다면
                visited[i] = visited[now_Node] + 1 # '이전 도시의 방문 리스트값 + 1' 저장
                queue.append(i)
        
for _ in range(M): # 그래프 데이터 저장
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X) # 너비 우선 탐색

for i in range(N + 1): # 방문 거리가 K인 노드를 정답 리스트에 더함
    if visited[i] == K:
        answer.append(i)

if not answer: # 정답 출력
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)