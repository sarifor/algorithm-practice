# for 문의 경우
a = [1.2, 2.5, 3.7, 4.6] # 리스트
for i in range(len(a)):
    a[i] = int(a[i])
print(a) # [1, 2, 3, 4]


# map 함수의 경우 (더 간단)
b = [1.2, 2.5, 3.7, 4.6] # 리스트
b = list(map(int, a))
print(b) # [1, 2, 3, 4]

c = list(map(str, range(10))) # 리스트 외의 반복 객체
print(c) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# input().split()과 map
d = input().split() # 10 20 입력
print(d) # ['10', '20'] (input().split()은 리스트를 반환)

e = map(int, input().split()) # 10 20 입력
print(e) # <map object at 0x0000017AACB6BFA0>
print(list(e)) # [10, 20]


# 리스트를 변수 두 개에 저장
f, g = [10, 20]
print(f) # 10
print(g) # 20

h, i = map(int, input().split()) # 10 20 입력
print(h) # 10
print(i) # 20

j = input().split() # 10 20 입력
k = map(int, j)
l, m = k # map 객체는 이터레이터라서 변수 여러 개에 저장하는 언패킹이 가능하므로, list(k)를 생략
print(l) # 10
print(m) # 20