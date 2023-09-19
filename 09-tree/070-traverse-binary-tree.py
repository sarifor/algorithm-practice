# Backjoon 1991
'''
1. Preorder traversal
The root node of the subtree is visited first.
Then the left subtree is traversed.
At last, the right subtree is traversed.

2. Inorder traversal
The left subtree is traversed first.
Then the root node for that subtree is traversed.
Finally, the right subtree is traversed.

3. Postorder traversal
The left subtree is traversed first.
Then the right subtree is traversed.
Finally, the root node of the subtree is traversed.
'''

import sys
input = sys.stdin.readline
N = int(input()) # 노드 개수
tree = {} # 딕셔너리

for _ in range(N):
  root, left, right = input().split() # 루트 노드, 왼쪽 노드, 오른쪽 노드
  tree[root] = [left, right] # 딕셔너리에 트리 데이터 저장

def preOrder(now): # 루트-왼쪽-오른쪽 순
  if now == '.':
    return # 자식 노드가 없는 경우 리턴
  print(now, end='')
  preOrder(tree[now][0])
  preOrder(tree[now][1])

def inOrder(now): # 왼쪽-루트-오른쪽 순
  if now == '.':
    return # 자식 노드가 없는 경우 리턴
  inOrder(tree[now][0])
  print(now, end='')
  inOrder(tree[now][1])

def postOrder(now): # 왼쪽-오른쪽-루트 순
  if now == '.':
    return # 자식 노드가 없는 경우 리턴
  postOrder(tree[now][0])
  postOrder(tree[now][1])
  print(now, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')