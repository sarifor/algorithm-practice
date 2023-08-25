# Backjoon 1516

from collections import deque

N = int(input()) # 건물 수
A = [[] for _ in range(N + 1)] # 건물 데이터 저장 인접 리스트
indegree = [0] * (N + 1) # 진입 차수 리스트
selfBuild = [0] * (N + 1) # 자기 자신을 짓는 데 걸리는 시간 저장 리스트

for i in range(1, N + 1): # 건물의 수만큼 반복
    # 인접 리스트 데이터 저장
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
        A[preTemp].append(i)
        indegree[i] += 1 # 진입 차수 리스트 데이터 저장

queue = deque()

for i in range(1, N + 1): # 건물 수만큼 반복
   if indegree[i] == 0:
      queue.append(i)

result = [0] * (N + 1) # 위상 정렬 결과를 저장할 배열

while queue: # 위상 정렬 수행
   now = queue.popleft()
   for next in A[now]:
      indegree[next] -= 1
      result[next] = max(result[next], result[now] + selfBuild[now])
      if indegree[next] == 0:
         queue.append(next)

for i in range(1, N + 1): # 위상 정렬 결과 출력
   print(result[i] + selfBuild[i])