n=input().lower().split()
a="aeiou"
mc=0
for i in n[0]:
    if i in a:
        mc+=1
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    if mc>c:
        mc=c
print(mc)