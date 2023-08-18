# Backjoon 1541
# Run the plus operations first,
# and subtract all the resulting values from the leading value.

answer = 0
A = list(map(str, input().split("-")))


def mySum(i):
  sum = 0
  temp = str(i).split("+")
  for i in temp:
    sum += int(i)
  return sum


for i in range(len(A)):
  temp = mySum(A[i])
  if i == 0:
    answer += temp
  else:
    answer -= temp

print(answer)