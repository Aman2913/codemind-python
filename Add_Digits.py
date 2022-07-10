n=int(input())
while True:
    s=0
    while n>0:
        p=n%10
        s+=p
        n//=10
    if len(str(s))==1:
            print(s)
            break
    else:
        n=s