n=input().lower()
n = n.split()
c=0
a=['a','e','i','o','u']
for i in n:
    if i[0] in a :
        c+=1
print(c)
        