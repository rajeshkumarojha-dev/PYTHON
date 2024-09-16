
import math

# ---------------
# APPROACH-1
# ---------------

def area_circle(r):
    Area = math.pi*r**2
    circumference = 2*math.pi*r
    return Area,circumference

radius = int(input("Enter Radius: "))

areaOfCircle,CircumferenceOfCircle = area_circle(radius)

print("-"*40)
print("Circle of radus is: {}".format(radius))
print("-"*40)

print("area of circle is : %0.1f " %(areaOfCircle)) 
print("circumference of circle is: %0.1f" %(CircumferenceOfCircle))
print("-"*50)


# ---------------
# APPROACH-2
# ---------------

def circle():
    radius = int(input("Enter Radius: "))
    Area = math.pi*radius**2
    circumference = 2*math.pi*radius
    print("-"*50)
    print("Area of circle: %0.1f" %(Area))
    print("Circumference of circle: %0.1f" %(circumference))
    print("-"*50)
circle()


# ---------------
# APPROACH-3
# ---------------

def area_circle(radius):
    Area = math.pi*radius**2
    circumference = 2*math.pi*radius
    print("-"*50)
    print("Area of circle : %0.1f" %(Area))
    print("Circumference of circle : %0.1f" %(circumference))
    print("-"*50)

CircleRadius = int(input("Enter radius value of circle: "))

area_circle(CircleRadius)




