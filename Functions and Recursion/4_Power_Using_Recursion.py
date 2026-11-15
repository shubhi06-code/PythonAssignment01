def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

if base == 0 and exponent < 0:
    print("Zero cannot have a negative exponent")
else:
    print("Result:", power(base, exponent))
