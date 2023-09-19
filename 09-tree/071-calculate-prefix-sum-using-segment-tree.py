# Backjoon 2042

import sys
input = sys.stdin.readline
N, M, K = map(int, input().split()) # 수의 개수, 변경 횟수, 구간 합 횟수
treeHeight = 0 # 트리 높이
length = N # 리프 노드 개수

# 트리 높이 구하기
# 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
    length //= 2 # Divides the variable with floor division and assigns the new amount to the variable.
    treeHeight += 1

# 트리 크기 구하기
# 2의 'treeHeight + 1' 승
# Q. length = 8일 때 treeSize가 16이 아니라 32가 나오는 이유는?
treeSize = pow(2, treeHeight + 1)

# 리프 노드 시작 인덱스
leftNodeStartIndex = treeSize // 2 - 1

# 인덱스 트리 저장 리스트
tree = [0] * (treeSize + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

#초기 트리 생성
setTree(treeSize - 1)

# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

# M + K만큼 반복
for _ in range(M + K):
    question, s, e = map(int, input().split()) # 질의 유형, 시작 인덱스, 종료 인덱스
    if question == 1: # 데이터 변경
        changeVal(leftNodeStartIndex + s, e)
    elif question == 2: # 구간 합
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))