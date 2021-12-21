basic=eval(input("Enter the basic pay drawn by the employee: "))
agp=basic*0.5
da=(basic+agp)*0.5
ta=(basic+agp)*0.15
total=round(basic+agp+da+ta,2)
print('The total salary drawn by the employee= ',total)