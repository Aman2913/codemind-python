t=int(input())
n=list(map(int,input().split()))
a=t//2
for i in range(t-1,a-1,-1):
    print(n[i],end=" ")
for i in range(0,a):
    print(n[i],end=" ")
