# Backjoon 1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split()) # 노드 개수, 질의 개수
parent = [0] * (N + 1)

def find(a):
    if a == parent[a]: # 대표 노드가 자기 자신이면, 자기 자신을 반환
        return a
    else:
        # 대표 노드가 자기 자신이 아니면, '대표 노드 = 자기 자신'이 될 때까지 반복하고(재귀),
        # 대표 노드에 도달하면 재귀 함수를 빠져나오면서 거치는 모든 노드값을 대표 노드값으로 변경(경로 압축)
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a # a, b를 하나의 집합으로 합치며, a를 대표 노드로 함

def checkSame(a, b): # 두 노드가 같은 집합에 속해 있는지를, 각각의 대표 노드 일치 여부로 확인
  a = find(a)
  b = find(b)
  if a == b:
      return True
  return False    

for i in range(0, N + 1): # 대표 노드 배열 초기화는 해당 노드의 값으로 함
    parent[i] = i

for i in range(M): # 각 질문에 대해
    question, a, b = map(int, input().split()) # 질문 유형, 노드 a, 노드 b
    if question == 0: # 질문 유형 0이면, 집합 합침
        union(a, b)
    else: # 질문 유형 1이면, 같은 집합의 노드인지 확인
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")