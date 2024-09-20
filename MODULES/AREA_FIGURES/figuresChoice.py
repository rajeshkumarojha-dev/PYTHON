from figuresMenu import menu
from areaOfRectangles import area as ar
from areaOfTriangle import area as at
from areaOfSquares import area as sa
from areaOfCircle import area as ac
import sys

while(True):
    menu()
    ch = input("Enter Choice: ")
    match(ch.lower()):

        case "r":
            ar()
        case "t":
            at()
        case 's':
            sa()
        case "c":
            ac()
        case "e":
            print("-"*40)
            print("<<< Thanx for Using >>>")
            print("-"*40)
            sys.exit()
        case _:
            print("-"*40)
            print("Enter wrong input.... Try Again !!!!")
            print("-"*40)

