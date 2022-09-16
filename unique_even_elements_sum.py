n = int(input())
x = list(map(int,input().split()))
temp = []
s = 0
for i in x:
    if i not in temp and i%2==0:
        temp.append(i)
        s+=i
print(s)