# Baekjoon 1874
# Push natural numbers from 1 to N in ascending order to a stack, and pop it appropriately to create a given array.
# Pop if the top value of the stack is equal to the value of the given array, and stop operations if it becomes larger than that.

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())
  
stack = []
num = 1
result = True
answer = ""

for i in range(N): 
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:  
            print("NO")
            result = False
            break
        else: # n == su
            answer += "-\n"

if result:
    print(answer)