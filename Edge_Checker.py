a,b=map(int,input().split())
if((a+1==b)or(b+1==a)or(a-1==b)or(b-1==a)or(a==10)or(b==1)and(a==1)or(b==10)):
    print('Yes')
else:
    print('No')