n=int(input())
x=list(map(int,input().split()))
f=0
for i in range(n-2):
    if (x[i]+x[i+1])!=x[i+2]:
        f=0
        break
    else:
        f=1
if f==1:
    print('yes')
else:
    print('no')