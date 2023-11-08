import sys

N = int(sys.stdin.readline())
first_List = list(map(int,sys.stdin.readline().split(' ')))


M = int(sys.stdin.readline())
second_List = list(map(int,sys.stdin.readline().split(' ')))

while len(second_List)>1:
    ans = second_List.pop()
    if ans in first_List:
        print(1)
    else:
        print(0)
