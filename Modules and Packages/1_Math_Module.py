import math
number = float(input("Enter a non-negative number: "))
base = float(input("Enter base for power: "))
exponent = float(input("Enter exponent: "))
angle = float(input("Enter angle in degrees: "))

if number < 0:
    print("Square root and factorial require a non-negative number")
else:
    print("Square root:", math.sqrt(number))

    if number.is_integer():
        print("Factorial:", math.factorial(int(number)))
    else:
        print("Factorial requires an integer")

print("Power:", math.pow(base, exponent))
radians = math.radians(angle)
print("Sine:", math.sin(radians))
print("Cosine:", math.cos(radians))
print("Tangent:", math.tan(radians))
