correct_password = "Python@123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break

    attempts += 1
    print("Incorrect password")

if attempts == 3:
    print("Blocked after 3 failures")
