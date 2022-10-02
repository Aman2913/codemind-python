s = input().lower()
v = ['a','e','i','o','u']
temp = []
for i in v:
    if i not in s and i not in temp:
        temp.append(i)
if len(temp)==0:
    print(0)
for i in sorted(temp):
    print(i,end=' ')