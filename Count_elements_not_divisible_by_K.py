n,k=map(int,input().split())
c=0
x=list(map(int,input().split()))
for i in range(n):
    if x[i]%k!=0:
        c+=1
print(c)