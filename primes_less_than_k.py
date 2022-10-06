def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
c=0
x=list(map(int,input().split()))
k=int(input())
for i in x:
    if i<=k and prime(i):
        c+=1
print(c)