from figuresMenu import menu
from figures import rarea, tarea, sarea, carea
import sys

while(True):
    menu()
    ch = input("Enter Choice: ")
    match(ch.lower()):

        case "r":
            rarea()
        case "t":
            tarea()
        case 's':
            sarea()
        case "c":
            carea()
        case "e":
            print("-"*40)
            print("<<< Thanx for Using >>>")
            print("-"*40)
            sys.exit()
        case _:
            print("-"*40)
            print("Enter wrong input.... Try Again !!!!")
            print("-"*40)

