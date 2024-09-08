# ---------------
# APPROACH-1
# ---------------

def calculate_simple_interest(principle,rate,time):
    calculate_interest = principle*rate*time/100
    Total_Amount = principle+calculate_interest
    return calculate_interest , Total_Amount

principle = int(input("Enter principle amount: "))
rate = int(input("Enter interest_rate amount: "))
time = int(input("Enter time_period amount: "))

calculateInterest,Total_Amount = calculate_simple_interest(principle,rate,time)


print("-"*40)
print("Principle Amount = {}".format(principle))
print("Interest Rate = {}".format(rate))
print("Time Period = {}".format(time))
print("-"*40)
print("Interest : {}".format(calculateInterest))
print("TotalAmount : {}".format(Total_Amount))
print("-"*40)

# ---------------
# APPROACH-2
# ---------------

def calculate_simple_interest():
    principle = int(input("Enter principle amount: "))
    rate = int(input("Enter interest_rate amount: "))
    time = int(input("Enter time_period amount: "))

    calculate_interest = principle*rate*time/100
    Total_Amount = principle+calculate_interest

    print("-"*40)
    print("Principle Amount = {}".format(principle))
    print("Interest Rate = {}".format(rate))
    print("Time Period = {}".format(time))
    print("-"*40)

    print("Interest : {}".format(calculate_interest))
    print("TotalAmount : {}".format(Total_Amount))

calculate_simple_interest()
print("-"*40)

# ---------------
# APPROACH-3
# ---------------

def calculate_simple_interest(principle,rate,time):
    calculate_interest = principle*rate*time/100
    Total_Amount = principle+calculate_interest
    print("Interest : {}".format(calculate_interest))
    print("TotalAmount : {}".format(Total_Amount))

  
principle = int(input("Enter principle amount: "))
rate = int(input("Enter interest_rate amount: "))
time = int(input("Enter time_period amount: "))


print("-"*40)
print("Principle Amount = {}".format(principle))
print("Interest Rate = {}".format(rate))
print("Time Period = {}".format(time))
print("-"*40)

calculate_simple_interest(principle,rate,time)
print("-"*40)
