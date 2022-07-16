n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    s=0
    temp=x[i]
    while temp:
        s=s*10+temp%10
        temp//=10
    print(s,end=' ')
        