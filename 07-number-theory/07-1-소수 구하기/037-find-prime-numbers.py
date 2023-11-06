# Backjoon 1929

import math
M, N = map(int, input().split())
A = [0] * (N + 1) # 크기가 N + 1인 리스트를 선언

for i in range(2, N + 1): # 리스트의 값은 각각의 인덱스값으로 채움
    A[i] = i

print(A)

# N을 2 ~ 루트 N의 정수로 나눠보는 것만으로 N이 소수인지 아닌지를 판단할 수 있음
# N에 1과 N 외의 약수가 있다고 가정했을 때, 그중 적어도 하나는 루트 N 이하라는 성질에 기반
for i in range(2, int(math.sqrt(N)) + 1): # for i in range(2, int(N ** 0.5) + 1): 
    if A[i] == 0:
        continue
    for j in range(i + i, N + 1, i):
        A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])