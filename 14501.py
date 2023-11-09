import sys

List = [[0,0]]
total_Price = []

N = int(sys.stdin.readline())
for i in range(N):
    T, P = map(int,sys.stdin.readline().split(" "))
    List.append([T,P])

for i in range(N+1): 
    total = i+1
    price = 0
    print(List)
    while total < N+1 :
        price += List[total][1]
        total += List[total][0]
    total_Price.append(price)

print(max(total_Price))

