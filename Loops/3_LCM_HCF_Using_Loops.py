a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

if x == 0 and y == 0:
    print("HCF and LCM are undefined for both numbers zero")
else:
    smaller = min(x, y)
    hcf = 1

    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i

    lcm = 0 if x == 0 or y == 0 else abs(a * b) // hcf

    print("HCF:", hcf)
    print("LCM:", lcm)
