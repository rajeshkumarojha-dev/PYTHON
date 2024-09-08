
# ---------------
# APPROACH-1
# ---------------

def rectangle(length,breadth):
    area = length*breadth
    cicumference = 2*(length*breadth)
    return area,cicumference

len = int(input("Enter length of rectangle: "))
bread = int(input("Enter breadth of rectangle: "))

AreaOfRectangle,CircunferenceOfRectangle = rectangle(len,bread)

print("Area of Rectangle: {}".format(AreaOfRectangle))
print("Circumference of Rectangle: {}".format(CircunferenceOfRectangle))

# ---------------
# APPROACH-2
# ---------------

def rectangle():
    
    length = int(input("Enter length of rectangle: "))
    breadth = int(input("Enter breadth of rectangle: "))
    area = length*breadth
    cicumference = 2*(length*breadth)
    print("-"*50)
    print("Area of Rectangle: {}".format(area))
    print("Circumference of Rectangle: {}".format(cicumference))
    print("-"*50)

rectangle()

# ---------------
# APPROACH-3
# ---------------

def rectangle(length,breadth):
    area = length*breadth
    cicumference = 2*(length*breadth)
    print("-"*50)
    print("Area of Rectangle: {}".format(area))
    print("Circumference of Rectangle: {}".format(cicumference))
    print("-"*50)

len = int(input("Enter length of rectangle: "))
bread = int(input("Enter breadth of rectangle: "))

rectangle(len,bread)

