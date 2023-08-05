# Backjoon 1920
# 데이터가 정렬되어 있는 상태에서 원하는 값을 찾는다.
# 대상 데이터의 중앙값과 찾고자 하는 값을 비교해,
# 데이터의 크기를 절반씩 줄이면서 대상을 찾고,
# '중앙값 == 타깃 데이터'일 때 탐색을 종료한다.

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]

    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)