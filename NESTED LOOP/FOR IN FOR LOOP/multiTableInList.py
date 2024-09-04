
n = int(input("Enter how many table want to print: "))

lst=[]
for i in range(1,n+1):
    num = int(input("Enter {} value : ".format(i)))
    lst.append(num)
else:
    print("-"*40)
    print("Given Mustiple Table is: {}".format(lst))

    for val in lst:
        print("-"*40)
        print("MULTITABLE OF: {}".format(val))
        print("-"*40)

        for j in range(1,11):
            print("{}X{}={}".format(val,j,val*j))
