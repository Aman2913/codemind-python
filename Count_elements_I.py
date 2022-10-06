n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
temp=[]
c=0
for i in n1:
    if (i in m1) and (i not in temp): 
        temp.append(i)
        c+=1
print(c)        