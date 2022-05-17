n=int(input())
i=n*n
sum=0
while i>0:
    d=i%10
    sum=sum+d
    i=i//10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')