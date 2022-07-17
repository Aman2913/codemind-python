n=int(input())
x=list(map(int,input().split()))
s=0
m=[]
for i in x:
    if x.count(i)==i and  i not in m:
        s+=i
        m.append(i)
if len(m)==0:
    print(-1)
else:
    print('%.2f'%(s/len(m)))