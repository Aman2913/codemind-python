n=int(input())
for i in range(1,n+1):
    temp=i
    r=0
    while temp>0:
        r=r*10+temp%10
        temp//=10
if r==i:
    print("True")
else:
    print("False")
