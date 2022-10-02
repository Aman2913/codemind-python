n=input().split()
a=["a","e","i","o","u"]
mc=0
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    if mc<c:
        mc=c
print(mc)