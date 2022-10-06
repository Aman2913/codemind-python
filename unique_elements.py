n=int(input())
x=list(map(int,input().split()))
c=[]

for i in x:
    if i not in c:
        c.append(i)
        print(i,end=" ")