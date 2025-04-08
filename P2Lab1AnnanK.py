#Kenneth Annan
#2/21/25
#P2Lab1
#Using Math Expressions
#I used the video tutorial linked in blackboard.
import math

#Grab Radius from User
radius = float(input("Enter the Radius: "))

#Circumference, Diameter, and Area

cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display
print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")