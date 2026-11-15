values = (10, 20, 30, 40, 50)

first, second, third, fourth, last = values
first, last = last, first

result = (first, second, third, fourth, last)

print("Tuple after swapping first and last elements:", result)
