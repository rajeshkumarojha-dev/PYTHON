
n = int(input("Enter value: "))

i=1
while(i<n+1):
    print("Outer while loop value is {}".format(i))
    i+=1

    for j in range(3,0,-1):
        print("\t Inner for loop value is: {}".format(j))
        j=j-1
    else:
        print("\t for loop completed.......")
else:
    print("While loop completed.......")