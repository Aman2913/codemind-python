n=int(input())
x=list(map(int,input().split()))
m=[]
for i in x:
    if i==x.count(i) and i not in m:
        m.append(i)
        print(i,end=' ')
if len(m)==0:
    print(-1)
