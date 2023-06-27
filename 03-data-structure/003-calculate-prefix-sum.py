# Baekjoon 11659

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo): # Repeat quizNo times
    s, e = map(int, input().split()) # These are counted from 1 when input, while counted from 0 when used as prefix_sum's index
    print(prefix_sum[e] - prefix_sum[s-1])
