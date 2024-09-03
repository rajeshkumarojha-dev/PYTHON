
n = int(input("Enter value: "))

i=1
while(i<=n):
    print("Outer value is {}".format(i))
    i=i+1

    j=1
    while(j<=3):
        print("\t Inner value is {}".format(j))
        j=j+1
    else:
        print("\t Inner while loop completed.......")
else:
    print("Outer while loop completed.....")