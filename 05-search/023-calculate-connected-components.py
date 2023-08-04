# Baekjoon 11724

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split()) # 노드 개수, 에지 개수
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
   visited[v] = True # 1에 2, 5가 연결되어 있다면, 현재 노드(1)를 방문 기록 하고
   for i in A[v]: # 현재 노드의 연결 노드(2, 5) 중
      if not visited[i]: # 방문하지 않은 노드로(예: visited[2] == False)
         DFS(i) # DFS 실행

for _ in range(m):
    s, e = map(int, input().split()) # 인접 리스트에 그래프 데이터 저장
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1): # n의 개수만큼 반복하며
    if not visited[i]: # 방문하지 않은 노드가 있다면
      count += 1 # 연결 개수 값 1 증가하고
      DFS(i) # DFS 실행

print(count)