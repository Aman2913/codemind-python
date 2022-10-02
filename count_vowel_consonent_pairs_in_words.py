n=input().lower().split()
s="aeiouAEIOU"
c=0
for i in n:
    for j in range(len(i)//2):
        if i[j] in s and i[-(j+1)] not in s:
            c+=1
        if i[j] not in s and i[-(j+1)] in s:
            c+=1
print(c)  