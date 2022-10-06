n=int(input())
x=list(map(int,input().split()))
b=sum(x)
avg=b//n
c=0
for i in range(n):
    if x[i]>=avg:
        c+=1
print(c)        