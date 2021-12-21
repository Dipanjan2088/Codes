row1=int(input('Enter the number of rows for 1st matrix: '))
col1=int(input('Enter tne number of column for 1st matrix: '))
row2=int(input('Enter the number of rows for 2nd matrix: '))
col2=int(input('Enter tne number of column for 2nd matrix: '))
if col1==row2:
    matrix1=[0]*row1
    for i in range(0,row1):
        r1=[0]*col1
        print('Enter {} integer for {} Row for 1st Matrix: '.format(col1,i))
        for j in range(0,col1):
            r1[j]=eval(input())
        matrix1[i]=r1

    matrix2=[0]*row2
    for i in range(0,row2):
        r2=[0]*col2
        print('Enter {} integer for {} Row for 2nd Matrix: '.format(col2,i))
        for j in range(0,col2):
            r2[j]=eval(input())
        matrix2[i]=r2
    result=[[0]*col2]*row1
    print('The 1st Matrix is: ')
    for i in range(0,row1):
        print(matrix1[i])
    print('The 2nd Matrix is: ')
    for i in range(0,row2):
        print(matrix2[i])
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print('The result is: ')
    for r in result:
        print(r)
else:
    print('Multiplication not possible!')