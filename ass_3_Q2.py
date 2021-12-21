y = int(input("Enter the year: "))
if (y % 4)==0 and (y % 100)!=0 or (y % 400)==0:
    print('{0} is a leap year'.format(y))
else:
    print('{0} is not a leap year'.format(y))