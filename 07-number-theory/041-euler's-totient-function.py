# Backjoon 11689

import math
N = int(input()) # 현재 소인수 구성
result = N # 서로소 개수

for p in range(2, int(math.sqrt(N)) + 1): # 제곱근까지만 진행
    if N % p == 0: # 현재 값이 소인수라면
        result -= result / p # 결괏값 = 결괏값 - 결괏값 / 현재 값
        while N % p == 0: # N에서 현재 소인수 내역을 제거. 2^7*11이라면 2^7을 없애고 11만 남김
            N /= p

if N > 1: # 반복문에서 제곱근까지만 탐색했으므로, 1개의 소인수가 누락되는 케이스 처리
    result -= result / N

print(int(result))