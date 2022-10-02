n=input().split()
a="aeiou"
mc=0
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    if mc<c:
        mc=c
wc=0        
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1            
    if c==mc:
        wc+=1
print(wc)    