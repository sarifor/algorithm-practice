# =: Assign value
a = [1, 2, 3] # Assign value
print(a) # [1, 2, 3]


# ==: Compare values
print(10 == 10) # True
print(1 == 1.0) # True
print('10' == 10) # False # "Python에선 ==로 값 비교 시 데이터 타입 변환까진 안 해줌"

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a == c) # True


# is: Compare objects
print(1 is 1) # True # 값(숫자)를 비교할 때는 is가 아닌 비교 연산자를 사용
print(1 is 1.0) # False # 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다르기 때문

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True
print(a is c) # False