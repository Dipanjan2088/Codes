s=int(input("Enter an integer: "))
t=s
sum=0
while s>0:
    r=s%10
    sum=sum*10+r
    s=s//10
print('The reverse value is: ',sum)
if(sum==t):
    print('{} this is a palindrome'.format(t))
else:
    print('{} this is not a palindrome'.format(t))    
