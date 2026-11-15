salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

salary_ok = salary >= 30000
credit_ok = credit_score >= 700
age_ok = 21 <= age <= 60

if salary_ok and credit_ok and age_ok:
    print("Approved")
elif sum([salary_ok, credit_ok, age_ok]) == 2:
    print("Conditionally Approved")
else:
    print("Rejected")
