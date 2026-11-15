def factorial(number):
    if number < 0:
        return None

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result

n = int(input("Enter a number: "))
answer = factorial(n)

if answer is None:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial:", answer)
