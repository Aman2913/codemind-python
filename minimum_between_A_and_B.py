n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
flag=0
for i in range(n):
    if x[i]>=a and x[i]<=b:
        c.append(x[i])
        flag=1
        
if flag!=1:
    print(-1)
else:
    print(min(c))