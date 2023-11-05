# Backjoon 2751
# Divide the array A into two, 
# select smaller value comparing two temp arrays,
# save it into array A,
# and check if any element was left.

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return
    
    m = int(s + (e - s) / 2)
    print("Start: " + str(s) + '\n')
    print("End: " + str(e) + '\n')
    print("Mid: " + str(m) + '\n')

    merge_sort(s, m)
    merge_sort(m + 1, e)

    print("Start after func.: " + str(s) + '\n')
    print("End after func.: " + str(e) + '\n')

    for i in range(s, e + 1):
        tmp[i] = A[i]

    print("tmp after func.: " + str(tmp) + '\n')

    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

    print("tmp: " + str(tmp) + '\n')
    print("A: " + str(A) + '\n')
    print("----" + '\n')

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1): # 인덱스 1부터 시작
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1): # 인덱스 1부터 시작
    print(str(A[i]) + '\n')