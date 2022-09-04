def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
if prime(a):
    print("prime")
else:
    print("not a prime")