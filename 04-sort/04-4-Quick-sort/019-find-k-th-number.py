# Backjoon 11004
# Quick sort
# Quick-sort numbers in acsending order until pivot location is equal to K

import sys
input = sys.stdin.readline
N, K = map(int, input().split()) # 숫자 개수, K번째 수
A = list(map(int, input().split())) # 숫자 데이터 저장 배열

def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K: # pivot == k이면 퀵 정렬 종료
            return
        elif K < pivot: # k < pivot이면 왼쪽 그룹만 정렬
            quickSort(S, pivot -1, K)
        else: # k > pivot이면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K) 

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S, E):
    global A

    if S + 1 == E: # 데이터가 2개인 경우는 바로 비교하여 정렬
        if A[S] > A[E]:
            swap(S, E)
            return E

    M = (S + E) // 2 # 중앙값을 시작 위치와 swap
    swap(S, M)
    pivot = A[S]

    i = S + 1 # 시작점
    j = E # 종료점

    while i <= j: # i가 j와 같아질 때까지(만날 때까지)
        while pivot < A[j] and j > 0: # pivot보다 작은 수가 나올 때까지 j 감소
            j = j - 1
        while pivot > A[i] and i < len(A)-1: # pivot보다 큰 수가 나올 때까지 i 증가
            i = i + 1
        if i <= j: # pivot보다 작은 j와 pivot보다 큰 i를 swap
            swap(i, j)
            i = i + 1
            j = j - 1

    A[S] = A[j] # pivot을 둘이 만난 위치(i == j)와 swap
    A[j] = pivot
    return j

quickSort(0, N - 1, K - 1)
print(A[K - 1])