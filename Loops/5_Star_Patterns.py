n = int(input("Enter number of rows: "))

print("Triangle")
for i in range(1, n + 1):
    print("* " * i)

print("Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("Diamond")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * (2 * i - 1))
