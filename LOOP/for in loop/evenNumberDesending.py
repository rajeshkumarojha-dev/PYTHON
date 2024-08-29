n=int(input("Enter value want to print Even number: "))

if(n<0):
    print("{}is invalid number".format(n))
else:
    print("List of Even number in Desending order: {}".format(n))
    for i in range(n,0,-2):
        print(i)
    else:
        print("for loop completed")
print("program execution completed")