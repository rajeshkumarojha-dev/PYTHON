from tempConversionMenu import menu
from fahToCel import fahToCel as fc
from fahToKel import fahToKel as fk
from celToFah import celToFah as cf
from celToKel import celToKel as ck
from KelToFahn import kelToFah as kf
from KelToCel import kelToCel as kc
import sys

while(True):
    menu()
    ch = input("Enter choice: ")
    match(ch):
        case "1":
            fc()
        case "2":
            fk()
        case "3":
            cf()
        case "4":
            ck()
        case "5":
            kf()
        case "6":
            kc()
        case "7":
            print("<<<<< Thax for using >>>>>>")
            sys.exit()
        case _:
            print("Enter Wrong Input >>> Try Again .....")
