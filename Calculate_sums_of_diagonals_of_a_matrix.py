n=int(input())
mat=[]
s=0
s1=0
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    for j in range(n):
        if i==j:
            s+=mat[i][j]
            
        if i==n-j-1:
            s1+=mat[i][j]
print("Principal Diagonal:"+str(s))
print("Secondary Diagonal:"+str(s1))
    