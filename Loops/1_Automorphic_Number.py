number = int(input("Enter a number: "))

square = number * number
digits = len(str(number))

if square % (10 ** digits) == number:
    print(number, "is an Automorphic Number")
else:
    print(number, "is not an Automorphic Number")
