bank = "icici"
branch = "Bhubaneswar"

def simpleIntrest():
    principal = int(input("Enter Principle Amount: "))
    rate = int(input("Enter rate of interest: "))
    time = int(input("Enter Time Perod: "))

    interest= principal*rate*time/100
    TotalAmount = principal+interest
    print('-'*40)
    print("Bank name is =",bank)
    print("Branch is =",branch)
    print('-'*40)
    print("Principle Amount is: ",principal)
    print("Rate of Interest is: ",rate)
    print("Time Period is: ",time)
    print('-'*40)
    print("Total Interest is = ",interest)
    print("Total Amount is = ",TotalAmount)
    print('-'*40)

# simpleIntrest()

