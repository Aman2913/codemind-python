n=int(input())
flag=0
for i in range(n):
    for j in range(n):
        if i*i+j*j==n:
            print(True)
            flag+=1
            break
    if flag==1:
        break
else:
    print(False)
            