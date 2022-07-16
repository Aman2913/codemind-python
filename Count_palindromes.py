n=int(input())
c=0
x=list(map(int,input().split()))
for i in range(n):
    temp=x[i]
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==x[i]:
        c+=1
print(c)