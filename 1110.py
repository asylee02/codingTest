import sys
N = int(sys.stdin.readline())
ans = N
cnt = 0
while(True):
   a = ans // 10
   b = ans % 10
   c = (a+b) % 10
   ans = b*10+c
   cnt +=1
   if(ans == N): 
    break
print(cnt)