# Backjoon 2751
# "입력받은 그룹(A)의 복사본(temp)을 만들어, 
# 해당 복사본을 절반으로 쪼개어, 각각의 인덱스를 비교하고, 
# 더 작은 값을 A에 덮어씌움으로, 오름차순 정렬한다."

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return
    
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)

    for i in range(s, e + 1):
        tmp[i] = A[i]

    k = s
    index1 = s # 첫 번째 그룹의 인덱스
    index2 = m + 1 # 두 번째 그룹의 인덱스

    while index1 <= m and index2 <= e: # 첫 그룹의 m번째까지와 두 번째 그룹의 e번째까지 동안
        if tmp[index1] > tmp[index2]: # 첫 번째 그룹의 인덱스가 두 번째 그룹의 인덱스보다 크다면
            A[k] = tmp[index2] # (더 작은 값인) 두 번째 그룹의 값을 A 리스트에 넣고
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m: # 한쪽 그룹이 모두 선택된 후, 남아 있는 값 정리 (다음 index1)
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    
    while index2 <= e: # 한쪽 그룹이 모두 선택된 후, 남아 있는 값 정리 (2) (다음 index2)
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')