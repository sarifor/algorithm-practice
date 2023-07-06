# Baekjoon 2164
# Move the top card to the bottom using queue's FIFO.

from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1): # If arguments are 2 and 3+1, the range is 2 and 3.
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])