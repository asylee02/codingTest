import sys;

S1, S2, S3 = map(int, sys.stdin.readline().split())
List = []
ans = 0
cnt = 0
for i in range(1,S1+1):
    for j in range(1,S2+1):
        for k in range(1,S3+1):
            List.append(i+j+k)

for i in range(S1+S2+S3):
    count = List.count(i)
    if count>cnt :
        cnt=count
        ans=i
    elif List.count(i)==cnt :
        if(i<ans):
            ans=i

        

print(ans)
