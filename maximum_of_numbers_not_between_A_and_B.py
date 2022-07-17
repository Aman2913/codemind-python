n=int(input())
x=list(map(int,input().split()))
a,b=map(int,input().split())
m=0
for i in x:
    if (i<a or i>b):
        if m<i:
            m=i
if m==0:
    print(-1)
else:
    print(m)