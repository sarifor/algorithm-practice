# Backjoon 1717
# Add new sets to the disjoint set,
# merge disjoint sets to a single disjoint set using Union operation,
# find representative of a disjoint set using Find operation,
# and check if two sets are disjoint or not.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
  a = find(a)
  b = find(b)
  if a == b:
      return True
  return False    

for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")