'''n=int(input("Enter the number of terms: "))
a=0
b=1
count=1
print('Fibonacci series: ')
while(count<=n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1'''


n=int(input("Enter the number of terms: "))
a,b=0,1
print('Fibonacci series: ')
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1    