n=int(input("Enter value want to print odd number: "))

if(n<0):
    print("{}is invalid number".format(n))
else:
    print("List of odd number in Desending order: {}".format(n))
    for i in range(n,0,-2):

        # otherwise

        # if(i%2==0):
        # i=i-1
        
        i=i-1
        print(i)
    else:
        print("for loop completed")
print("program execution completed")