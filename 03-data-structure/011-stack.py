# Baekjoon 1874
# Push natural numbers from 1 to N in ascending order to a stack, and pop it appropriately to create a given array.
# Pop if the top value of the stack is equal to the value of the given array, and stop operations if it becomes larger than that.

N = int(input()) # 만들어야 하는 수열의 개수
A = [0]*N

for i in range(N):
    A[i] = int(input()) # 만들어야 하는 수열을 이루는 정수
  
stack = [] # 스택
num = 1
result = True
answer = ""

for i in range(N): # 만들어야 하는 수열의 개수만큼 반복
    su = A[i]
    if su >= num: # 구할 값이, 자연수보다 같거나 크면,
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else: # 구할 값이, 자연수보다 작으면,
        n = stack.pop() # 스택의 가장 위의 수를 빼 보고,

        # 스택의 '가장 위의 수'가 '만들어야 하는 수열의 수'보다 크면,
        # 자연수를 오름차순으로 스택에 넣었기 때문에,
        # 수열을 출력(pop)할 수 없으므로, 계산을 중지한다.
        if n > su:  
            print("NO")
            result = False
            break
        # n = su인 경우. n < su까진 가지 않는다.
        else:
            answer += "-\n"

if result:
    print(answer)