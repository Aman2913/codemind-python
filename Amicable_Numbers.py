n=int(input())
m=int(input())
s=0
s2=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,m):
    if m%j==0:
        s2+=j
if ((s2==n) and (s==m)):
    print('Amicable')
         
else:
    print('Not Amicable')