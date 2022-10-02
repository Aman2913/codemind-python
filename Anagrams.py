s1=(input())
s2=(input())
c=0
for i in s1:
    if i in s2 and i in s1:
        print(True)
        break
    else:
        print(False)
        break