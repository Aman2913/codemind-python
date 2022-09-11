n=int(input())
temp=n
sum=0
while temp:
    fact=1
    p=temp%10
    temp//=10
    for i in range(1,p+1):
        fact=fact*i
    sum+=fact
    # print(sum)
if sum==n:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")