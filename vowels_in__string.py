n=input()
r=["a","e","i","o","u"]
k=["A","E","I","O","U"]
temp=[]
for i in n:
    if (i in r or  i in k )and i not in temp:
        temp.append(i)
        print(i,end=" ")
if not bool(len(temp)):
    print(-1)