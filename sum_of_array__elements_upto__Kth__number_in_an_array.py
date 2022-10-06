n=int(input())
x=list(map(int,input().split()))
k=int(input())
c=0
for i in x:
    c+=i
    if i==k:
        break
print(c)    