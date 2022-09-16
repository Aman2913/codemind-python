a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    temp=i
    while temp:
        p=temp%10
        temp//=10
        if p==0:
            break
        if i%p==0:
            c+=1
    if c==len(str(i)):
        print(i,end=' ')