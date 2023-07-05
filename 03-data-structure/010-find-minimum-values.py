# Baekjoon 11003

from collections import deque
N, L = map(int, input().split()) # 데이터 개수, 최솟값 구하는 범위
mydeque = deque() # 데이터를 담을 덱 자료구조 
now = list(map(int, input().split())) # 주어진 숫자 데이터를 가지는 리스트

for i in range(N): # N만큼 반복
    # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거하고, 덱의 마지막 위치에 현재 값을 저장.
    # 덱을 이용하여 오름차순 정렬 효과를 봄.
    while mydeque and mydeque[-1][0] > now[i]: # 덱의 마지막 번째의 '값' 
        mydeque.pop()
    mydeque.append((now[i], i)) # (값, 인덱스) 순 저장

    # 덱의 1번째 위치에서부터 L의 '범위를 벗어난 값(now index-L <= index)'을 덱에서 제거  
    # "범위가 i+L+1 ~ i이니, 범위를 벗어난 값은 i - L까지가 된다"
    if mydeque[0][1] <= i - L: # 덱의 첫 번째 값의 '인덱스'
        mydeque.popleft()
    
    # 덱의 1번째 '값' 출력
    print(mydeque[0][0], end=' ')