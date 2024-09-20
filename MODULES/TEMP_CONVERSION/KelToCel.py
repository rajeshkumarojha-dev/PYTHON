def kelToCel():
    print("KEL TO CEL")
    K = int(input("Enter temp in term of KEL: "))
    c = (K-273.15)*(9/5)+32
    print('-'*40)
    print("Equi. temp in CEL: %0.1f" %(c))
# kelToCel()