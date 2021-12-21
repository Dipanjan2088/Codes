def wellbrackted(exp):
    stck=[]
    for i in exp:
        if i=='(':
            stck.append('(')
        if i==')':
            try:
                stck.pop()
            except IndexError:
                return False
    if len(stck)==0:
        return True
    else:
        return False
exp=input('Enter an expression: ')
if wellbrackted(exp):
    print(exp, 'is well brackted.')
else:
    print(exp, 'is not well brackted.')