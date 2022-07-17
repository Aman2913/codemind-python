a,b,c=map(int,input().split())
p=2*a*b*c*512
c=p//1024
print(str(c)+'KB')