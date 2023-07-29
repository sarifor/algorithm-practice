# Backjoon 10989

import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N): # N만큼 반복하며, count 리스트에 현재 수에 해당하는 index의 값 1 증가
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)