def lcm(a,b):
    s=max(a,b)
    while True:
        if s%a==0 and s%b==0:
            return s
        s+=max(a,b)
n=int(input())
h=list(map(int,input().split()))
d=lcm(h[0],h[1])
for i in range(1,n):
    d=lcm(d,h[i])
print(d)
    