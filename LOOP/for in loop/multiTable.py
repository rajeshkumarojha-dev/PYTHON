

n=int(input("Enter any number: "))

if(n<0):
    print("{} is invalid value".format(n))
else:
    print("Multiplication table of : {}".format(n))
    for i in range(1,11):
        print("{} X {} = {}".format(n,i,n*i))