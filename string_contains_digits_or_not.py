n=int(input())
for i in range(n):
    s=input()
    flag=0
    for j in list(s):
        if j.isdigit():
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print('No')
    else:
        print('Yes')