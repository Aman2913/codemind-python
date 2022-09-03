n=int(input())
for i in range(n):
    a=int(input())
    p=1
    for j in range(1,a+1):
        p=j*p
    print(p)