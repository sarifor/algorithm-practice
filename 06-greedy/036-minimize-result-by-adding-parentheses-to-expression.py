# Backjoon 1541

answer = 0
A = list(map(str, input().split("-"))) # 들어온 데이터를 '-' 기호를 기준으로 split


def mySum(i): # 더하기에 해당하는 부분에 괄호를 쳐서 먼저 모두 계산
  sum = 0
  temp = str(i).split("+")
  for i in temp:
    sum += int(i)
  return sum


for i in range(len(A)):  # 가장 앞에 있는 데이터 값에서, 더하기 연산으로 나온 결괏값들을 모두 빼기
  temp = mySum(A[i])
  if i == 0:
    answer += temp
  else:
    answer -= temp

print(answer)