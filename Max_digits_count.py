n=int(input())
x=list(map(int,input().split()))
a=max(x)
b=len(str(a))
c=0
for i in x:
    if len(str(i))==b:
        c+=1
print(c)        