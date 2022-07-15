n=int(input())
p=0
while 1:
    while n!=0:
        p+=(n%10)**2
        n//=10
    if p==1 or p==7:
        print(True)
        break
    elif p<10:
        print(False)
        break
    else:
        n=p
        p=0