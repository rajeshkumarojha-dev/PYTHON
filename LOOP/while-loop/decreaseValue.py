
n = int(input("Enter any value: "))
if(n<0):
    print("{} is invaid".format(n))
else:
    # i=n
    while(n>=1):
        print(n)
        n=n-1
    else:
        print("while loop completed")
print("program execution completed")