# Baekjoon 12891

checkList = [0] * 4 # 각 문자의 개수 조건
myList = [0] * 4 # 현재 각 문자의 개수
checkSecret = 0 # (A, C, G, T 중) 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 수

# 새로 들어오는 문자열 처리
def myadd(c):
    global checklist, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]: # 'A'가 지정한 개수만큼 있으면,
            checkSecret += 1 # 1개 문자가 개수 충족했다고 판단
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1
            
# 제거되는 문자열 처리
def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A': # A가 들어오면, checkSecret과 myList에서 A와 관련된 개수를 1 삭감
        if myList[0] == checkList[0]: 
            checkSecret -= 1
        myList[0] -= 1 
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

# S, P, A, checkList를 입력받음
S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# 값이 0이면 비밀번호 개수가 이미 만족되었다는 뜻이니, checkSecret을 1 늘림
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 P 부분 문자열 처리
for i in range(P):
    myadd(A[i])

# 4 자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호 개수
if checkSecret == 4: # A, C, G, T 각 문자의 개수가 모두 조건을 만족하면(4), 유효한 비밀번호로 판단
    Result += 1

# 한 칸씩 이동하면서 새로 들어오는 문자열과 제거되는 문자열을 처리
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)