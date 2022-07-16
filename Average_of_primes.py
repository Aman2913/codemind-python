def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
x=list(map(int,input().split()))
s=0
p=0
for i in range(n):
    if prime(x[i]):
        s+=x[i]
        p+=1
print('%.2f'%(s/p))


        
    