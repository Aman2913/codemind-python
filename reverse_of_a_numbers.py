n=int(input())
reverse_n=0
while(n>0):
    r=n%10
    reverse_n=(reverse_n*10)+r
    n=n//10
print('{}'.format(reverse_n))