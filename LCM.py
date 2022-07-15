n=list(map(int,input().split()))
if n[0]>n[1]:
    p=n[0]
else:
    p=n[1]
for i in range(1,p):
    if n[0]%i==0 and n[1]%i==0:
        hcf=i
lcm=(n[0]*n[1])/hcf
print(int(lcm))