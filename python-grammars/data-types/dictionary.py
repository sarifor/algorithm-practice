# 0. 리스트, 튜플
food = ['Takoyaki', 'Delicious', 350, 20231115]


# 1. Dictionary
food2 = {'name': 'Takoyaki', 'taste': 'Delicious', 'price': 350, 'expiration date': 20231115}


# 2. Don't allow duplicate key in dictionary
food3 = {'name': 'Ajifurai', 'name': 'Salad', 'taste': 'Delicious', 'price': 200, 'expiration date': 20231113}
print(food3['name']) # Salad


# 3. 딕셔너리의 키와 값으로 사용할 수 있는 자료형
# 3.1 키에 문자열, 정수, 실수, 불 사용 가능
boy = {15: 'age', 60.5: 'weight', True: 'student'}
print(boy[60.5]) # weight

# 3.2 값에 모든 자료형 사용 가능
boy2 = {15: 'age', 60.5: 'weight', True: 'student', 'hobby': {'first': 'Gaming', 'second': 'Excercise'}}


# 4. 반복문으로 딕셔너리의 키-값 쌍을 출력
# 4.1 키만 출력됨
for i in boy2:
  print(i, end=' ') # 15 60.5 True hobby

# 4.2 키, 값 출력
for k, v in boy2.items():
  print(k, v, end=' ') # 15 age 60.5 weight True student hobby {'first': 'Gaming', 'second': 'Excercise'}

# 4.3 키만 출력
for k in boy2.keys():
  print(k, end=' ') # 15 60.5 True hobby

# 4.4 값만 출력
for v in boy2.values():
  print(v, end=' ') # age weight student {'first': 'Gaming', 'second': 'Excercise'}