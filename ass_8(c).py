class MyException(Exception):
    pass

def rotatelist(l,n=1,d="Left"):
    rl=[]
    length=len(l)
    try:
        if n> l:
            raise MyException
        elif d=="Left":
            rl=l[n:length]+l[0:n]
        elif d=="Right":
            rl=l[l-n:l]+l[0:l-n]
    except MyException:
        print('The number of rotation is greater tha thy number of element')
        rl=l.copy()
    finally:
        return rl
l=[]
num=int(input("No. of elements: "))
for n in range(num):
    numbers=int(input('Enter numbers: '))
    l.append(numbers)
print(l)
n=int(input('Enter the no. of times the list will be rotated: '))
d=input('Enter the direction(Left/Right): ')
print(rotatelist(l,n,d))