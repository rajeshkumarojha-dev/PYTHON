s= """Arithmetic operations

        1. Addition 
        2. Substraction
        3. Multiplication
        4. Division
        5. Modulo Division
        6. Exponentiation

"""

print(s)

ch = input('Enter your Choice: ')

match(ch):
    case '1':
        print("ADDITION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a+b
        print("{} + {} = {}".format(a,b,result))
    case '2':
        print("SUBSTRACTION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a-b
        print("{} - {} = {}".format(a,b,result))

    case '3':
        print("MULTIPLICATION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a*b
        print("{} * {} = {}".format(a,b,result))

    case '4':
        print("DIVISION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a/b
        print("{} / {} = {}".format(a,b,result))

    case '5':
        print("MODULO DIVISION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a%b
        print("{} % {} = {}".format(a,b,result))

    case '6':
        print("EXPONENTIALTION")
        print('Enter any two number: ')
        a,b = int(input()),int(input())
        result = a**b
        print("{} ** {} = {}".format(a,b,result))

    case _:
        print("EXIT")
        print('Enter Wrong Choice....Try Again !')
print("program execution completed")
        