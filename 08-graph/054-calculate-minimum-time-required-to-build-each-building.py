# Backjoon 1516

from collections import deque

N = int(input()) # 건물 수
A = [[] for _ in range(N + 1)] # 건물 데이터 저장 인접 리스트
indegree = [0] * (N + 1) # 진입 차수 리스트
selfBuild = [0] * (N + 1) # 자기 자신을 짓는 데 걸리는 시간 저장 리스트

for i in range(1, N + 1): # 건물의 수만큼 반복
    # 데이터 입력받음
    # ex. [10, 1, -1]: 건물 짓는 데 걸리는 시간, 먼저 지어야 하는 건물들의 번호, 각 줄이 끝남을 표시
    inputList = list(map(int, input().split()))

    # 자기 자신 시간 리스트 데이터 저장
    selfBuild[i] = (inputList[0]) 
    
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
          break
        A[preTemp].append(i) # 인접 리스트 데이터 저장
        indegree[i] += 1 # 진입 차수 리스트 데이터 저장

queue = deque()

for i in range(1, N + 1):
   if indegree[i] == 0: # 진입 차수 리스트의 값이 0인 건물(노드)을 큐에 삽입
      queue.append(i)

result = [0] * (N + 1) # 정답 리스트

while queue: # 각 건물을 짓는 데 걸리는 최대 시간 업데이트
   now = queue.popleft()
   for next in A[now]:
      indegree[next] -= 1
      result[next] = max(result[next], result[now] + selfBuild[now])
      if indegree[next] == 0:
         queue.append(next)

# 정답 리스트에 자기 건물을 짓는 데 걸리는 시간을 더한 후, 정답 리스트를 차례대로 출력
for i in range(1, N + 1):
   print(result[i] + selfBuild[i])