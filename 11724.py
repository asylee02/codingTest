import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(' '))
adj = [[0]*N for _ in range(N)]

for i in adj:
    