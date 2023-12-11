# Queue

# 1. list로 구현

# 1.1 구현 -> list
q = [4, 5, 6]

# 1.2 요소 추가 -> 맨 뒤
q.append(7)
q.append(8)
print(q) # [4, 5, 6, 7, 8]

# 1.3 요소 꺼냄 -> 맨 앞
q.pop(0)
print(q) # [5, 6, 7, 8]


# 2. Queue로 구현

# 2.1 구현 -> queue.Queue()
import queue

q2 = queue.Queue()

# 2.2 요소 추가 -> 맨 뒤
q2.put(4)
q2.put(5)
q2.put(6)
# print(q2) # <queue.Queue object at 0x00000150B6AF77D0>
# print(len(q2)) # TypeError: object of type 'Queue' has no len()
print(q2.qsize()) # 3

# 2.3 요소 꺼냄 -> 맨 앞
q2.get()
print(q2.qsize()) # 2


# 3. deque로 구현
from collections import deque

# 3.1 구현 -> deque
q3 = deque([4, 5, 6])

# 3.2 요소 추가 -> 맨 뒤
q3.append(7)
q3.append(8)
print(q3) # deque([4, 5, 6, 7, 8])

# 3.3 요소 꺼냄 -> 맨 앞
q3.popleft()
print(q3) # deque([5, 6, 7, 8])