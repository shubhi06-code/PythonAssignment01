def natural_sum(n):
    if n <= 0:
        return 0
    return n + natural_sum(n - 1)

n = int(input("Enter n: "))

if n < 0:
    print("Enter a non-negative number")
else:
    print("Sum:", natural_sum(n))
