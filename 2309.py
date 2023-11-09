from itertools import combinations
import sys

List = []
ans = []
for _ in range(9):
    N = int(sys.stdin.readline())
    List.append(N)

for i in combinations(List, 7):
    if sum(i) == 100:
        ans =list(i)

ans.sort()
for i in range(7):
    print(ans[i])