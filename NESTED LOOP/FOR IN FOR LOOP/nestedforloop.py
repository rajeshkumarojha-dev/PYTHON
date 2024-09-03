n = int(input("Enter any vaalue: "))

for i in range(1,n+1):
    print("Outer value is {}".format(i))
    for j in range(1,4):
        print("\t inner value is {}".format(j))
    else:
        print("\t Inner loop is completed....")
else:
    print("Outer loop is completed.....")