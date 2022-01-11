f1=open('text12.txt','w')
n=int(input('Enter the nth term: '))
for i in range(2,n+1):
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            f1.write(str(i)+' ')
f1.close()