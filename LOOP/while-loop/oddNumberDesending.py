
n = int(input("Enter any value: "))

if(n<0):
    print("{} is invalid number".format(n))
else:
    # i=1
    if(n%2==0):
        n=n-1
    while(n >= 1):
        print(n)
        n = n-2
    else:
        print("While Loop ended")
print("program execution completed")