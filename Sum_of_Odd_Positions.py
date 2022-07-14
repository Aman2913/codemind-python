n=int(input())
x=list(map(int,input().split()))
s=0
for i in range(n):
    if i%2==1:
        s+=x[i]
print(s)