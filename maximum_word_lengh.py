s= input().split()

c = 0
for i in s:
    if len(i)>c:
        c = len(i)
        
print(c)