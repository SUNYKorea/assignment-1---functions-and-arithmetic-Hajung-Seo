# Name: Hajung Seo
# SBUID: 115265291

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   return float((5/9) * (fahrenheit - 32))

def what_to_wear(celsius):
    
    if(celsius < -10):
        print("Puffy jacket")
    elif(-10 <= celsius < 0):
        print("Scarf")
    elif(0 <= celsius < 10):
        print("Sweater")
    elif(10 <= celsius < 20):
        print("Light jacket")
    elif (20 <= celsius):
        print("T-shirt")
    else:
        print("Put a different degree, please.")
       

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

#import math
def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    Area = abs((((x1 * y2)+(x2 * y3)+(x3 * y1))-((x1 * y3)+(x2 * y1)+(x3 * y2)))/2)
    return Area

def euclidean_distance(x1, y1, x2, y2, x3, y3):
    #p1 = (x1,y1)
    #p2 = (x2,y2)
    #p3 = (x3,y3)

    #perimeter = math.dist(p1,p2) + math.dist(p2,p3) + math.dist(p1,p3)
    
    dis_P1P2 = (((x1 - x2)**2)+((y1 - y2)**2))**(1/2)
    dis_P2P3 = (((x2 - x3)**2)+((y2 - y3)**2))**(1/2)
    dis_P1P3 = (((x1 - x3)**2)+((y1 - y3)**2))**(1/2)
    return dis_P1P2, dis_P2P3, dis_P1P3

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return ((((x1 - x2)**2)+((y1 - y2)**2)) ** (1/2)) + ((((x2 - x3)**2)+((y2 - y3)**2)) ** (1/2)) \
          + ((((x1 - x3)**2)+((y1 - y3)**2)) ** (1/2))


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math
def deg2rad(deg):
    rad = (deg * math.pi) / 180
    return rad

def apothem(number_sides, length_side):
   n = number_sides
   s = length_side
   a = s / (2 * math.tan(math.radians(180 / n)))
   return a

def polygon_area(number_sides, length_side):
   n = number_sides
   s = length_side
   a = s / (2 * math.tan(math.radians(180 / n)))
   pol_area = (n * s * a) / 2
   return pol_area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))