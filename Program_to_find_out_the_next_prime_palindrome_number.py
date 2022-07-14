def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
def palindrome(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==n:
        return True
    return False
n=int(input())
a=n+1
while a:
    if prime(a) and palindrome(a):
        break
    a+=1
print(a)
