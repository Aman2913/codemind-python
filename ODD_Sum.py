n=int(input())
m=list(map(int,input().split()))
odd=0
for i in range(0,n):
    if m[i]%2==1:
        odd+=m[i]
print(odd)