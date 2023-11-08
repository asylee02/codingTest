from collections import deque
import sys

List = deque()

N = int(sys.stdin.readline())

for i in range(N):
    List.append(i+1)

while len(List)>1:
    List.popleft()
    List.append(List.popleft())

print(List[0])