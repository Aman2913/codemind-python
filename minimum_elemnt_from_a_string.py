n=input().split()
k=n[-1]
c=min(k)
if c.isupper():
    if c.lower() in k:
        print(c.lower())
    else:
        print(c)
else:
    print(c)