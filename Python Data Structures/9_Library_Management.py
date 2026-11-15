library = {"Python": 5, "Data Science": 3, "Machine Learning": 4}

print("Library:", library)

book = input("Enter book name: ")
quantity = int(input("Enter quantity to add: "))

if quantity < 0:
    print("Quantity cannot be negative")
else:
    library[book] = library.get(book, 0) + quantity
    print("Updated Library:", library)

book_to_issue = input("Enter book name to issue: ")

if book_to_issue in library and library[book_to_issue] > 0:
    library[book_to_issue] -= 1
    print("Book issued successfully")
else:
    print("Book not available")

print("Final Library:", library)
