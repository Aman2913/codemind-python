n=list(input())
v=input()

for i in n:
    if i==v:
        print(True)
        print(n.index(i))
        break
else:
    print(False)