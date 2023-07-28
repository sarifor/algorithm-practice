# Backjoon 11004

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S, E, K): # 시작, 종료, K
    global A
    if S < E:
        pivot = partition(S, E) # pivot을 구함
        if pivot == K: # pivot이 K이면, pivot 앞은 오름차순 정렬이 완료되었고, pivot 뒤로는 더 볼 필요가 없으므로 종료
            return
        elif K < pivot: # pivot이 K보다 크면, pivot의 왼쪽 부분에 K가 있으므로, 왼쪽만 정렬 수행
            quickSort(S, pivot -1, K)
        else: # pivot이 K보다 작으면, pivot의 오른쪽 부분에 K가 있으므로, 오른쪽만 정렬 수행
            quickSort(pivot + 1, E, K) 

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S, E):
    global A

    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
            return E

    M = (S + E) // 2 # 중앙값을 시작 위치와 swap하고, 시작 위치 값을 pivot으로 삼음
    swap(S, M)
    pivot = A[S]

    i = S + 1 # 시작점 i
    j = E # 종료점 j

    while i <= j: # pivot보다 작은 j와 pivot보다 큰 i를 발견하면 swap
        while pivot < A[j] and j > 0: 
            j = j - 1
        while pivot > A[i] and i < len(A)-1: 
            i = i + 1
        if i <= j: 
            swap(i, j)
            i = i + 1
            j = j - 1 # i와 j가 만난 위치

    A[S] = A[j] # i와 j가 만난 위치와 pivot을 swap
    A[j] = pivot
    return j # pivot 반환

quickSort(0, N - 1, K - 1)
print(A[K - 1])