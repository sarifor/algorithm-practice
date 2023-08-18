# Backjoon 1929

import math
M, N = map(int, input().split())
A = [0] * (N + 1) # 크기가 N + 1인 리스트를 선언

for i in range(2, N + 1): # 리스트의 값은 각각의 인덱스값으로 채움
    A[i] = i

print(A)

# 2부터 시작하고 현재 숫자가 지워진 상태가 아닌 경우,
# '현재 선택된 수'의 배수에 해당하는 수를 리스트에서 끝까지 탐색하면서 지움
# 처음으로 선택된 숫자는 지우지 않음
# 바꿔 말하면, N의 제곱근 이하의 수의 배수를 모두 제거하면, 1부터 N 사이의 소수를 구할 수 있음 //230818 이해 재시도
for i in range(2, int(math.sqrt(N)) + 1): # 'for i in range(2, N+1):'보다 시간이 덜 걸림
    if A[i] == 0:
        continue
    for j in range(i + i, N + 1, i):
        A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])