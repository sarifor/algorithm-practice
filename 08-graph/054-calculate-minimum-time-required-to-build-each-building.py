# Backjoon 1516
# Pick all the verticles with in-degree as 0,
# add them into a queue,
# remove a vertex from the queue,
# decrease in-degree by 1 for all its neighbouring nodes,
# update maximum time each neighbouring node needs,
# and if the in-degree of neighbouring nodes is reduced to 0, then add it to the queue.
# Repeat steps above until the queue is empty.

from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) 
selfBuild = [0] * (N + 1)

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0]) 
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
          break
        A[preTemp].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1, N + 1):
   if indegree[i] == 0:
      queue.append(i)

result = [0] * (N + 1)

while queue:
   now = queue.popleft()
   for next in A[now]:
      indegree[next] -= 1
      result[next] = max(result[next], result[now] + selfBuild[now])
      if indegree[next] == 0:
         queue.append(next)

for i in range(1, N + 1):
   print(result[i] + selfBuild[i])