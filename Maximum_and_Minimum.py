n=int(input())
x=list(map(int,input().split()))
m=[]
for i in x:
    if x.count(i)==i and i not in m:
        m.append(i)
if len(m)==0:
    print(-1)
else:
    print(min(m),max(m),end='')