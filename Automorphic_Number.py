n=int(input())
square=n**2
l=len(str(n))
m=square%pow(10,l)
if m==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')