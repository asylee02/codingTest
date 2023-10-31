import sys

N = int(sys.stdin.readline())
List = []
answer=[]
ans = ''
for i in range(N):
    name = sys.stdin.readline()
    List.append(name[0])
result = list(set(List))

for i in result:
    if(List.count(i)>=5):
        answer.append(i)

if(len(answer)==0):
    print("PREDAJA")
else:
    answer.sort()
    ans = ''.join(answer)
    print(ans)
