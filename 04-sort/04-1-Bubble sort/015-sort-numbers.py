# Baekjoon 2750
# Bubble sort
# After each iteration, one less element(the last one) is needed to be compared
# until there are no more elements left to be compared.

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]: # When i == 3, only A[0] and A[1] is compared.
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])