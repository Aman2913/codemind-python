num=int(input())
square=num**2
num_of_digits=len(str(num))
last_digits= square%pow(10,num_of_digits)
if last_digits==num:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')