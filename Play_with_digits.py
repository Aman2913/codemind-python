n=int(input())
x=list(map(int,input().split()))
q=0
for i in range(n):
    s=0
    temp=x[i]
    s+=temp%10
    temp//=10
    p=(s+temp)
    q+=p
print(q)
    