# Backjoon 1934
# Find LCM(Least Common Multiple) using GCD(Greatest Common Divisor).

def gcd(a, b):
    if b == 0:
      return a
    else:
      return gcd(b, a % b)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))