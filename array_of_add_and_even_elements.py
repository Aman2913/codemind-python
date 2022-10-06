n=int(input())
x=list(map(int,input().split()))
for i in x:
    if i%2==1:
        print(i,end=" ")
for j in x:
    if j%2==0:
        print(j,end=" ")