import sys

N, M = map(int, sys.stdin.readline().strip().split())
List=[]
cnt_X =0
cnt_Y =0
for i in range(N):
    X = sys.stdin.readline().strip()
    List.append(X)

for i in List:
    if(i.count('X')==0):
        cnt_X+=1

for i in range(M):
    cnt=0
    for k in List:
        if(k[i]=='X'):
            cnt+=1
            break
    if(cnt==0):
        cnt_Y+=1

if(cnt_X-cnt_Y >0):
    print(cnt_X)
else: print(cnt_Y)
