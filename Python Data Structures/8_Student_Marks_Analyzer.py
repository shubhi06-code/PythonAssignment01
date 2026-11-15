students = {"Aarav": 85, "Diya": 92, "Rohan": 67, "Meera": 74, "Kabir": 28}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)
failures = [name for name, marks in students.items() if marks < 33]

print("Student Marks:", students)
print("Topper:", topper)
print("Topper Marks:", students[topper])
print("Average Marks:", average)
print("Failed Students:", failures)
