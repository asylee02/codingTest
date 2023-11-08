import sys
N, M = map(int, sys.stdin.readline().split(' '))
first=()
second=()
ans = 0

first = set(map(int, sys.stdin.readline().split(' ')))
second = set(map(int, sys.stdin.readline().split(' ')))


first_ = first.copy()
second_= second.copy()


for i in range(len(first)):
    a = first.pop()
    if a in second:
        second.remove(a)

ans += len(second)



for i in range(len(second_)):
    a = second_.pop()
    if a in first_:
        first_.remove(a)


ans += len(first_)

print(ans)