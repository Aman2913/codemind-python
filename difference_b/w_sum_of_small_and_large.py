s=input().split()
c=0
for i in s:
    p=(abs(ord(max(i))-ord(min(i))))
    c+=p
print(c)