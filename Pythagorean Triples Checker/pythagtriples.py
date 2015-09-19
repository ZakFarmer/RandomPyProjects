import time

def isTriple(a, b, c):
    if ((a ** 2) + (b ** 2) == (c ** 2)):
        return True
    else:
        return False

print("Type in the sides of the triangle (any order)")
input1 = int(input("Side 1: "))
input2 = int(input("Side 2: "))
input3 = int(input("Side 3: "))

sides = [input1, input2, input3]

hypotenuse = max(sides)
sides.remove(hypotenuse)
side1 = sides[0]
side2 = sides[1]

print("\n" + "Thinking..." + "\n")
time.sleep(1)
print("Hypotenuse:", hypotenuse)
time.sleep(1)
print("Other sides:", side1, "and", side2)
time.sleep(1)

if (isTriple(side1, side2, hypotenuse) == True):
    print("The triangle is a pythagorean triple!")
else:
    print("The triangle is not a pythagorean triple!")
