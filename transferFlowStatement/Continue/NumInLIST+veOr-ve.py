

list = [12,13,-9,14,-6,0,18,-15]

lst = []
lst1 =[]
for val in list:
    if(val<0):
        lst.append(val)
else:
    print(lst)


for val in list:
        if(val>0):
            lst1.append(val)
else:
    print(lst1)