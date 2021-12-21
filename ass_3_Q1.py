n1 = eval(input("Enter the 1st number:"))
n2 = eval(input("Enter the 2st number:"))
n3 = eval(input("Enter the 3st number:"))
if (n1>=n2) and (n1>=n3):
    large=n1
elif(n2>=n1) and (n2>=n3):
    large=n2
else:
    large=n3
print('The greatest number is:',large)