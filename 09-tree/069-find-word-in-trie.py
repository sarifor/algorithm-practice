# Backjoon 14425
'''
1. Initialize Trie data structure with root node(NULL).

2. To insert a word, iterate over the length of it and check if the value is NULL or not in the array of pointers at the current character of the word.
2-1. If it's NULL then, make a new node, point the current character to this newly created node, and move the currentNode to the newly created node.
2-2. If not, move the currentNode to the next node.
2-3. When reaching the last character, mark it as a leaf node.

3. To find a word, convert it to characters and then compare every character with the trie node from the root node.
3-1. If the current character is present in the node, move forward to its children.
3-2. Repeat the above process until all characters are found.
'''

from sys import stdin
input = stdin.readline

# Node 클래스 생성
class Node(object):
  def __init__(self, isEnd):
    self.isEnd = isEnd
    self.childNode = {}

# Trie 클래스 생성
class Trie(object):
  def __init__(self):
    self.parent = Node(None)  # 루트 노드는 항상 공백 유지

  def insert(self, string):
    nowNode = self.parent
    temp_length = 0
    for char in string:  # 문자열을 탐색하여
      # 자식 노드에 없는 문자면
      # ex. apple에 이어 air를 넣었을 때, i, r이 자식 노드에 없는 문자에 해당
      if char not in nowNode.childNode:
        nowNode.childNode[char] = Node(char)  # 신규 생성하고
      nowNode = nowNode.childNode[char]  # 자식 노드 문자로 이동
      temp_length += 1
      if temp_length == len(string):  # 이번 문자열의 마지막 문자면
        nowNode.isEnd = True  # 마지막 문자 표시

  def search(self, string):
    nowNode = self.parent
    temp_length = 0
    for char in string:  # 문자열을 탐색하여
      if char in nowNode.childNode:
        nowNode = nowNode.childNode[char]
        temp_length += 1
        #마지막 문자까지 모두 존재하고, 마지막 문자에 isEnd가 True인 경우, True 리턴
        if temp_length == len(string) and nowNode.isEnd == True:
          return True
      else:
          return False
    return False
    
N, M = map(int, input().split())  # 집합 S의 문자열 개수, 검사할 문자열 개수
myTrie = Trie()  # Trie 생성

for _ in range(N):
  word = input().strip()
  myTrie.insert(word)

result = 0

for _ in range(M):
  word = input().strip()
  if myTrie.search(word):
    result += 1

print(result)