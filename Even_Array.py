n=int(input())
x=list(map(int,input().split()))
# print(x)
for i in range(n):
    if x[i]%2!=0:
        print(False)
        break
else:
    print(True)
        