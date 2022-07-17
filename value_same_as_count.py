n=int(input())
x=list(map(int,input().split()))
m=[]
c=0
for i in x:
    if i==x.count(i) and i not in m:
        m.append(i)
        c+=1
print(c)