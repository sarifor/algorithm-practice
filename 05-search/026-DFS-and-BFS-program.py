# Backjoon 1260
# 원래 문제의 DFS 부분 삭제

from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M): # 그래프 저장
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1): # 그래프 오름차순 정렬
    A[i].sort() # 예: [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]는 [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]로 정렬됨

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]: # 예: [1, 4]이면, queue에는 1과 4 개개로 들어감
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N + 1)
BFS(Start)