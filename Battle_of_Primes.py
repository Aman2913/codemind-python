def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
for i in range(1,1000000):
    if prime(n1+n2+i):
        print(i)
        break