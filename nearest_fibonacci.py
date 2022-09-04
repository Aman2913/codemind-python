n=int(input())

w=[0,1]
a=0
b=1
c=0
for i in range(n):
    d=a+b
    w.append(d)
    if d>n:
        break
    a=b
    b=d
after= w[len(w)-1]
before = w[len(w)-2]

da=after-n
db=n-before
if da==db:
    print(before,after)
elif da>db:
    print(before)
else:
    print(after)