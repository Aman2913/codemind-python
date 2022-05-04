n=int(input())
odd=0
x=list(map(int,input().split()))
for i in range(n):
    if (x[i]%2!=0):
        odd+=1
if(odd<=2):
    print("YES")
else:
    print("NO")