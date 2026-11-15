from datetime import datetime, date

current_datetime = datetime.now()
print("Current date and time:", current_datetime.strftime("%d-%m-%Y %H:%M:%S"))

birth_date_text = input("Enter date of birth (DD-MM-YYYY): ")
birth_date = datetime.strptime(birth_date_text, "%d-%m-%Y").date()
today = date.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Age:", age)
