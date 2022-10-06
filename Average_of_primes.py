def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
s=0
c=0
x=list(map(int,input().split()))
for i in x:
    if prime(i):
        s+=i
        c+=1
avg=s/c
print("{:.2f}".format(avg))