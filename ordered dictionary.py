from collections import *
N = int(input("Enter number:"));
d = OrderedDict();
d['BANANA FRIES']=0
d['POTATO CHIPS']=0
d['APPLE JUICE']=0
d['CANDY']=0
for i in range(N):
    item = input("Enter item:").split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(d.get(itemName)):
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
for i in d.keys():
    print(i, d[i])