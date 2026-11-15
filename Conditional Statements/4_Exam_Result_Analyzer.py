marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks of subject {i}: "))
    marks.append(mark)

if any(mark < 33 for mark in marks):
    print("Fail")
else:
    percentage = sum(marks) / 5
    print("Pass")
    print("Percentage:", percentage)

    if percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    elif percentage >= 40:
        print("Third Division")
    else:
        print("Pass")
