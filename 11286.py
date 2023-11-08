import sys
import heapq
N= int(sys.stdin.readline())
List = []

for i in range(N):
    M = int(sys.stdin.readline())
    if M!=0:
        if M<0:
            heapq.heappush(List,[-M,M])

        else: 
            heapq.heappush(List, [M,M])
    else:
        if len(List)>0:
            print(heapq.heappop(List)[1])
        else:
            print(0)
