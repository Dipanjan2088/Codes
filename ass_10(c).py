f1=open('text2.txt','w')
n=int(input('Enter the nth value: '))
a,b=0,1
sum=0
count=1
while(count<=n):
    f1.write(str(sum)+' ')
    a=b
    b=sum
    sum=a+b
    count+=1
f1.close()