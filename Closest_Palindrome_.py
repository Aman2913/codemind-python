def palindrome(n):
    rev=0
    temp=n
    while temp:
        rev=rev*10+temp%10
        temp//=10
    if rev==n:
        return True
    return False
n=int(input())
a=n+1
b=n-1
while a:
    if palindrome(a):
        break
    a+=1
while b:
    if palindrome(b):
        break
    b-=1
p=a-n
q=n-b
if p==q:
    print(b,a)
elif p>q:
    print(b)
else:
    print(a)