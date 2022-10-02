n = int(input())

x = list(map(int,input().split()))

b= len(str(x[0]))
for i in x:
    if len(str(i))<b:
        b=len(str(i))

c = 0
for i in x:
    if b==len(str(i)):
        c+=1
print(c)