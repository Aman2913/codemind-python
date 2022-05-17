n=int(input())
for i in range(1,n):
    if i**2==n:
        print(True)
        break
else:
    print(False)