subjects = ("Python", "Mathematics", "DBMS", "Operating Systems", "Computer Networks")

print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))

subject = input("Enter a subject to find its index: ")

if subject in subjects:
    print("Index:", subjects.index(subject))
else:
    print("Subject not found")
