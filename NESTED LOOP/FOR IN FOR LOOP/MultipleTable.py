n = int(input("Enter value : "))

for i in range(1,n+1):
    print("-"*40)
    print("Multiplication table of {}".format(i))
    print("-"*40)

    for num in range(1,11):
        print("\t {}X{}={}".format(i,num,num*i))
    else:
        print("Inner loop completed.......")
else:
    print("Outer Loop Completed..........")