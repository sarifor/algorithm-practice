# Backjoon 1934

def gcd(a, b): # 최대공약수 구하기
    if b == 0:
      return a
    else:
      return gcd(b, a % b)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b) # 주어진 두 수와, 두 수의 최대공약수로, 최소공배수 구하기
    print(int(result))