s=input().split()
for i in s:
    p=(abs(ord(max(i))-ord(min(i))))
    print(p,end=" ")