# def count(ele):
#     if ele[-1] == '.':
#         ele = ele[0:len(ele) - 1]
#     if ele in d:
#         d[ele] += 1
#     else:
#         d.update({ele: 1})
# Sentence = input("Enter the sentance: ")
# d = {}
# lst = Sentence.split()
# for ele in lst:
#     count(ele)
# for allKeys in d:
#     print (allKeys , ":" , d[allKeys], end = " ")


s=input('Enter the sentance: ')
l2=[]
l3=[]
l1=s.split()
for n in l1:
    if n.isalpha():
        l2.append(n)
        l3.append(l1.count(n))
t1=tuple(zip(l2,l3))
s1=set(t1)
d1=dict(s1)
print(d1)
