n,m=map(int,input().split())
c=0
x=set(list(map(int,input().split())))
y=set(list(map(int,input().split())))
p=x&y
print(len(p))