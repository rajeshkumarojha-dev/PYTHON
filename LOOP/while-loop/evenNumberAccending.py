
n = int(input("Enter any value: "))

if(n<0):
    print("{} is invalid number".format(n))
else:
    i=0
    while(i<=n):
        print(i)
        i=i+2
    else:
        print("While Loop ended")
print("program execution completed")