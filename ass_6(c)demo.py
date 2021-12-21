print("Enter order of 1st matrix: ")
m,n = list(map(int,input().split()))
print("Enter Row wise values ")
mat1 = []
for i in range(m) :
    print("Enter row",i,"value: ")
    row = list(map(int,input().split()))
    mat1.append(row)
print("Enter order of 2nd matrix: ")
p,q = list(map(int,input().split()))
print("Enter Row wise values ")
mat2 = []
for j in range(p) :
    print("Enter row", j ,"value: ")
    row = list(map(int,input().split()))
    mat2.append(row)
print("Matrix 1: ",mat1)
print("Matrix 2: ",mat2)
resultant = []
for i in range(m):
    row = []
    for j in range(q):
        row.append(0)
    resultant.append(row)
print("Matrix Multiplication: ")
for i in range(m):
    for j in range(q):
        for k in range(n) :
            resultant[i][j] += mat1[i][k] * mat2[k][j]            
for row in resultant:
    print(row)