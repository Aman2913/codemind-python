def ln(n):
    if n==0:
        return 1
    if n<0:
        n*=-1
    c=0
    while n:
        c+=1
        n//=10
    return c
n=int(input())
x=list(map(int,input().split()))
mc=0
for i in x:
    if ln(i)>mc:
        mc=ln(i)
for i in x:
    if ln(i)==mc:
        print(i,end=" ")