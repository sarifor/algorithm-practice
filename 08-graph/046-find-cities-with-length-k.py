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
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)
        
for _ in range(M): # 그래프 데이터 저장
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X) # 너비 우선 탐색

for i in range(N + 1): # 방문 리스트에서 값이 거리 K와 같은 경우, 해당 노드를 정답 리스트에 저장
    if visited[i] == K:
        answer.append(i)

if not answer: # 정답 출력
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)