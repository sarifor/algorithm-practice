# Baekjoon 1427

import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)): #i번째 요소와 i번째 이후(j) 요소를 비교하여 최댓값을 찾고,
        if A[j] > A[Max]:
            Max = j
    if A[i] < A[Max]: # 최댓값과 i번째 요소의 위치를 바꾼다.
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])