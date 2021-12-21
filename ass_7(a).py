s1=input('Enter the statement: ')
up,lw=0,0
for i in s1:
    if 65<=ord(i)<=90:
        up+=1
    if 97<=ord(i)<=122:
        lw+=1
print('{0} upper case and {1} lower case is present in the statement.'.format(up,lw))