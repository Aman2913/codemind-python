n=int(input())
x=list(map(int,input().split()))
s=0
for i in range(n):
    if x[i]%2==0:
        break
    p=x[i]
    if x[i]<=p:
        s+=x[i]
print(s)    