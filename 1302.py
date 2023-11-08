import sys

book = {}
best = []
N = int(sys.stdin.readline())

for i in range(N):
    M=sys.stdin.readline().strip()
    if M in book:
        book[M]+=1
    else:
        book[M]=1

selling = max(book.values())

for i in book:
    if book[i] == selling:
        best.append(i)

best.sort()

print(best[0])