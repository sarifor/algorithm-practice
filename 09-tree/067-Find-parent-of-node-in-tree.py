# Backjoon 11725
# Store the tree data into adjacency list,
# and put nodes from the root node into DFS function.
# If the node has unvisited child,
# Store its parent in answer list.
# If children are all visited,
# go up to the parent node and search again.

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())  # 노드 개수
visited = [False] * (N + 1)  # 방문 기록 저장 리스트
tree = [[] for _ in range(N + 1)]  # 그래프 데이터 저장 인접 리스트
answer = [0] * (N + 1)  # 부모 노드 저장 정답 리스트

for _ in range(1, N):  # 인접 리스트에 트리 데이터 저장
  n1, n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)


def DFS(number):
  visited[number] = True
  for i in tree[number]:  # 현재 노드의 연결 노드 중
    if not visited[i]:  # 미방문 노드가 있다면
      answer[i] = number  # 미방문 노드의 부모 노드를 정답 리스트에 저장
      DFS(i)  # 자식 노드가 모두 방문한 노드면, 부모 노드로 올라가 다시 탐색


DFS(1)

for i in range(2, N + 1):
  print(answer[i])  # 정답 리스트 출력