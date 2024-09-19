bank = "icici"
branch = "Bhubaneswar"

def simpleIntrest(principal,rate,time):
    interest= principal*rate*time/100
    TotalAmount = principal+interest
    print("Bank name is =",bank)
    print("Branch name is =",branch)
    print("Principle Amount is: ",principal)
    print("Rate of Interest is: ",Rate_of_interest)
    print("Time Period is: ",time_period)

    print("Total Interest is = ",interest)
    print("Total Amount is = ",TotalAmount)
    return interest,TotalAmount

principal = int(input("Enter Principle Amount: "))
Rate_of_interest = int(input("Enter rate of interest: "))
time_period = int(input("Enter Time Perod: "))

# Amount = simpleIntrest(principal,Rate_of_interest,time_period)



