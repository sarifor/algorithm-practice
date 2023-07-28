# Backjoon 11399

N = int(input())
A = list(map(int, input().split()))
S = [0]*N

for i in range(1, N): # 삽입 정렬로 데이터를 오름차순 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]: # 정렬 대상 값보다 작은 값을 발견하면, 그 값의 바로 뒤를 삽입 위치로 삼고, break
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1): # i가 4이고, insert_point가 2라면, 범위는 4, 3
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N): # 각자의 인출시간 구하기
    S[i] = S[i-1] + A[i] # S[i] = A[0] + A[1] + ... + A[i]

sum = 0

for i in range(0, N): # 모든 사람의 인출시간 구하기
    sum += S[i]

print(sum)