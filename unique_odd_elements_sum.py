n=int(input())
x=set(list(map(int,input().split())))
c=0
for i in x:
    if i%2==1:
        c+=i
print(c)    