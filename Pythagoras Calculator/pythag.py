import math

print("Type in the opposite and adjacent sides of the triangle")
side1 = int(input("Side 1: "))
side2 = int(input("Side 2: "))
hypotenuse = int(math.sqrt((side1 ** 2) + (side2 ** 2)))

print("The hypotenuse of this triangle is:", hypotenuse)

