n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    temp=x[i]
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    print(rev,end=' ')
        