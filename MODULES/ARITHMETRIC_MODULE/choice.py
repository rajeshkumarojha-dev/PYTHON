from arithmeticMenu import menu
from sum import sum
from substraction import substraction
from multiplication import Multiplication
from division import division
from ModDivision import ModDivision
from Exponentiation import Exponentiation
import sys

while(True):
    menu()
    ch = input("Enter Your Choice: ")
    match(ch):
        case "1":
            sum()
        case "2":
            substraction()
        case "3":
            Multiplication()
        case "4":
            division()
        case "5":
            ModDivision()
        case "6":
            Exponentiation()
        case "7":
            print("<<<<<< Tanx for Using >>>>>>")
            sys.exit()
        case _:
            print("Enter wrong choice..... Try Again !!!!!!!")
