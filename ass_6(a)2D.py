row=int(input('Enter the number of rows: '))
col=int(input('Enter tne number of column: '))
matrix=[0]*row
for i in range(0,row):
    r=[0]*col
    print('Enter {} integer for {} Row: '.format(col,i))
    for j in range(0,col):
        r[j]=int(input())
    matrix[i]=r
max1=list()
min1=list()
for i in matrix:
    print(i)
    max1=max1+[max(i)]
    min1=min1+[min(i)]
print('The largest element is: ',max(max1))
print('The smallest element is: ',min(min1))