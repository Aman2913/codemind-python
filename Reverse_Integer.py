n=int(input())
n = str(n)
if n[0] == '-':
    a = int('-' + n[-1:0:-1])
    print(a)
else:
    a = int(n[::-1])
    print(a)
    
