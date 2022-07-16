n=int(input())
x=list(map(int,input().split()))
k=int(input())
s=0
for i in range(n):
    if x[i]<=k:
        s+=x[i]
print(s)    