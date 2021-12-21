a=eval(input('Enter the 1st number: '))
b=eval(input('Enter the 2nd number: '))
c=eval(input('Enter the 3rd number: '))
if a!=0:
    d=(b**2)-(4*a*c)
    if d>0:
        r1=(-b+(d**0.5))/(2*a)
        r2=(-b-(d**0.5))/(2*a)
        print('The solutions are {0:0.2f} and {1:0.2f}'.format(r1,r2))
    elif d==0:
            r= -b/(2*a)
            print('The solution is',r)

    else:
        d=-1*d
        rl=((-b)/(2*a))
        im=((d**0.5)/(2*a))
        R1=complex(rl,im)
        R2=R1.conjugate()
        print('The solutions are {0} and {1}'.format(R1,R2))
else:
    print('It is not a quadratic equation')        