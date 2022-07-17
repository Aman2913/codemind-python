n=int(input())
x=list(map(int,input().split()))
k=int(input())
m=[]
for i in x:
    if x.count(i)==k and i not in m:
        m.append(i)
        print(i,end=' ')
if len(m)==0:
    print(-1)