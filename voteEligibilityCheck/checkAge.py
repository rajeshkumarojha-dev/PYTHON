n = int(input("Enter age: "))

if(n>=18):
    print("You can vote")
else:
    print("you con't vote")

# --------------------
# using while loop 
# --------------------

while(True):
    n = int(input("Enter age: "))
    if(n>=18):
        print("You can vote")
        break
    else:
        print("you con't vote")