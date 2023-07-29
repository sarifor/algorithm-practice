# Backjoon 10989
# Take a count array to store the count of each number.
# Store the count of each number in the count array.
# If any number repeats itself, simply increase its count.
# Print each index of count array as much as its element.

import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)