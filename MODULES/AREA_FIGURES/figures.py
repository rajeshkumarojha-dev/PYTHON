def rarea():
    length = int(input("Enter Length: "))
    breadth = int(input("Enter Breadth: "))

    areaOfRect = length*breadth
    print("Area of rectangular: {}".format(areaOfRect))
# rarea()

def tarea():
    Base = int(input("Enter Base: "))
    Height = int(input("Enter Height: "))

    areaOfTriangle = (1/2)*Base*Height
    print("Area of Triangle: {}".format(areaOfTriangle))
# tarea()

def sarea():
    side = int(input("Enter Side: "))

    areaOfsquares = side*side
    print("Area of Squares: {}".format(areaOfsquares))
# sarea()

def carea():
    radius = int(input("Enter radius: "))

    areaOfCircles = 3.14*radius**2
    print("Area of Circles: {}".format(areaOfCircles))
# carea()