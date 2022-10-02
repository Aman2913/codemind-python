n,m=map(int,input().split())
x=list(map(int,input().split()))
# print(x,m)
c=0
for i in x:
    if i<0:
        i*=-1
    if len(str(i))==m:
        c+=1
print(c)        