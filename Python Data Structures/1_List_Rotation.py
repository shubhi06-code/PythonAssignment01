numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
k = int(input("Enter number of positions: "))

if numbers:
    k = k % len(numbers)
    left_rotated = numbers[k:] + numbers[:k]
    right_rotated = numbers[-k:] + numbers[:-k] if k else numbers[:]

    print("Left rotation:", left_rotated)
    print("Right rotation:", right_rotated)
else:
    print("The list is empty")
