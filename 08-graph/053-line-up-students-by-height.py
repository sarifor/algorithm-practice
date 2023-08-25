from collections import deque

N, M = map(int, input().split())  # 노드 수, 비교 횟수
A = [[] for _ in range(N + 1)]  # 인접 리스트 배열
indegree = [0] * (N + 1)  # 진입차수 배열

for i in range(M):
  S, E = map(int, input().split())  # 인접 리스트 데이터
  A[S].append(E)  # 인접 리스트 데이터 저장
  indegree[E] += 1  # 진입차수 데이터 저장

queue = deque()

for i in range(1, N + 1):  # 진입 차수 0인 노드를 큐에 삽입
  if indegree[i] == 0:
    queue.append(i)

while queue:
  now = queue.popleft()
  print(now, end=' ')  # 현재 노드값 출력
  for next in A[now]:
    indegree[next] -= 1  # 현재 노드의 타깃 노드의 진입 차수값 1 감소
    if indegree[next] == 0:  # 타깃 노드의 진입 차수가 0이면
      queue.append(next)  # 큐에 타깃 노드 추가
