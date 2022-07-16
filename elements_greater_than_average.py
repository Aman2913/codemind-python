n=int(input())
x=list(map(int,input().split()))
s=sum(x)
p=s//n
c=0
for i in range(n):
    if x[i]>=p:
        c+=1
print(c)        