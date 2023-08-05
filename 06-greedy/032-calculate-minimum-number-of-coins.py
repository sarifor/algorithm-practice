# Backjoon 11047

N, K = map(int, input().split()) # 동전 개수, 목표 금액
A = [0] * N # 동전 데이터 리스트

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N - 1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)