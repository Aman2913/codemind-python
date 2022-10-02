s=input().split()
a=["a","e","i","o","u"]
# for
for i in s:
    c=0
    for j in i:
        if j in a:
            c+=1
    print(c,end=" ")