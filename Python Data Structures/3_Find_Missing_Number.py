n = int(input("Enter n: "))
numbers = list(map(int, input(f"Enter {n - 1} numbers from 1 to {n}: ").split()))

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

print("Missing number:", expected_sum - actual_sum)
