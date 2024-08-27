s = """ TEMPRETURE CONVERTION CALCULATOR

        1. F to C
        2. F to K
        3. c to F
        4. c to K
        5. k to F
        6. k to C
        7. EXIT

"""

print(s)

ch = input("Enter your Choice: ")

match(ch):
    case "1":
        print("F to C")
        F = float(input("Enter temp in term of F: "))
        c = (F-32)*(5/9)
        print("""
              ANSWER
              """)
        print("Given temp in term of F: {}".format(F))
        print("Eqivalent temp in term of c: {}".format(c))

    case "2":
        print("F to K")
        F = float(input("Enter temp in term of F: "))
        K = (F-32)*(5/9)+273.15
        print("""
              ANSWER
              """)
        print("Given temp in term of F: {}".format(F))
        print("Eqivalent temp in term of K: {}".format(K))

    case "3":
        print("C to F")
        C = float(input("Enter temp in term of C: "))
        F = C*(9/5)+32
        print("""
              ANSWER
              """)
        print("Given temp in term of C: {}".format(C))
        print("Eqivalent temp in term of F: {}".format(F))

    case "4":
        print("C to K")
        C = float(input("Enter temp in term of C: "))
        K = C+273.15
        print("""
              ANSWER
              """)
        print("Given temp in term of C: {}".format(C))
        print("Eqivalent temp in term of K: {}".format(K))

    case "5":
        print("K to F")
        K = float(input("Enter temp in term of K: "))
        F = K-273.15
        print("""
              ANSWER
              """)
        print("Given temp in term of K: {}".format(K))
        print("Eqivalent temp in term of F: {}".format(F))

    case "6":
        print("K to C")
        K = float(input("Enter temp in term of K: "))
        C = (K-273.15)*(9/5)+32
        print("""
              ANSWER
              """)
        print("Given temp in term of K: {}".format(K))
        print("Eqivalent temp in term of c: {}".format(C))
    
    case _:
        print("EXIT")
        print('Enter Wrong Choice... TryAgain !!!')
        
print("Program Execution Completed")