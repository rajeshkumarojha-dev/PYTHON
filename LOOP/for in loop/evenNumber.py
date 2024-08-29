n=int(input("Enter value want to print Even number: "))

if(n<0):
    print("{}is invalid number".format(n))
else:
    print("List of Even number with in: {}".format(n))
    for i in range(0,n+1,2):
        print(i)
    else:
        print("for loop completed")
print("program execution completed")