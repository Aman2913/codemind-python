s1=input().lower().replace(' ','')
s2=input().lower().replace(' ','')
c=0
temp =[]
for i in s1:
    if i  not in s2 and i not  in temp:
        temp.append(i)

for i in s2:
    if i not  in s1 and i not  in temp:
        temp.append(i)
for i in sorted(temp):
    print(i,end="")