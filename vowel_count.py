s=input().lower()
c=0
for l in s:
    if l in 'aeiou':
        c+=1
print(c)