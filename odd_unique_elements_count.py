n=int(input())
x=list(set(list(map(int,input().split()))))
c=0
for i in x:
    if i%2==1:
        c+=1
print(c)        