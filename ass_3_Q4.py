unit=int(input("Enter the unit: "))
if (0<=unit<=200):
    rate = unit*0.50
elif (201<=unit<=400):
    rate = 100+unit*0.65
elif (401<=unit<=600):
    rate = 200+unit*0.80
elif (unit>=601):
    rate = 300+unit*1.00
print('Electricity Bill = {0:0.2f}'.format(rate))