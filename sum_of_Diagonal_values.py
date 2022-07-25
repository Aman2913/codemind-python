n,m=map(int,input().split())
s=0
p=0
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
# print(mat)
for i in range(n):
    for j in range(m):
        if i==j:
            s+=mat[i][j]
        elif i+j==n-1:
            p+=mat[i][j]
print(s+p)
    