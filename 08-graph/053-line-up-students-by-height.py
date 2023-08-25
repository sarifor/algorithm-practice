# Backjoon 2252
# Pick all the verticles with in-degree as 0,
# add them into a queue,
# remove a vertex from the queue and print it,
# decrease in-degree by 1 for all its neighbouring nodes,
# and if the in-degree of neighbouring nodes is reduced to zero, then add it to the queue.
# Repeat steps above until the queue is empty

from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)] 
indegree = [0] * (N + 1)

for i in range(M):
  S, E = map(int, input().split())
  A[S].append(E)
  indegree[E] += 1

queue = deque()

for i in range(1, N + 1):
  if indegree[i] == 0:
    queue.append(i)

while queue:
  now = queue.popleft()
  print(now, end=' ')
  for next in A[now]:
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)
