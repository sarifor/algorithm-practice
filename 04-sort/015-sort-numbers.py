# Baekjoon 2750

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(N-1): # If the start argument is omitted, it defaults to 0.
    for j in range(N-1-i):
        if A[j] > A[j+1]: # i가 3일 때, j는 0뿐이고, A[0]과 A[1]만 비교하게 됨 -> 데이터가 모두 정렬됨 -> 프로세스 종료
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])

# list.sort()
B = [5, 4, 3, 2, 1]
B.sort()
# print(B.sort()) # None
print(B) # [1, 2, 3, 4, 5]

# sorted()
C = [9, 8, 7, 6, 5]
print(sorted(C)) # [5, 6, 7, 8, 9]