l1  = list()
a = int(input("Enter the size of list: "))
for i in range(0,a):
    p=int(input())
    l1.append(p)
uniq_items = []
for x in l1:
    if x not in uniq_items:
        uniq_items.append(x)
print(uniq_items)

