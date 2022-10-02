n=int(input())
x=list(map(int,input().split()))
for i in x:
    if i<0:
        i*=-1
    print(len(str(i)),end=" ")