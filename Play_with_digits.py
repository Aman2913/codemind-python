n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
    while (i!=0):
        rem=i%10
        i//=10
        s+=rem
print(s)        