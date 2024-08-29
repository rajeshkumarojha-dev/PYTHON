

n = int(input("Enter number want to print natural numbers: "))

if(n<0):
    print("{}is invalid number".format(n))
else:
    square=0
    for s in range(1,n+1):
        print("\t{}".format(s**2))
        square += s**2
    else:
        print('-'*20)
        print("\t{}".format(square))
