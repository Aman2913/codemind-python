n=int(input())
x=list(map(int,input().split()))
m=[]
for i in x:
    if i not in m:
        m.append(i)
        print(i,end=' ')    