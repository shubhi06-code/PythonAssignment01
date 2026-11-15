numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List after removing duplicates:", unique_numbers)
