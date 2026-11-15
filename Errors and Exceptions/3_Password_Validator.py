class PasswordLengthError(Exception):
    pass

class UppercaseError(Exception):
    pass

class NumberError(Exception):
    pass

password = input("Enter password: ")

try:
    if len(password) < 8:
        raise PasswordLengthError("Password length must be at least 8 characters")
    if not any(character.isupper() for character in password):
        raise UppercaseError("Password must contain at least one uppercase letter")
    if not any(character.isdigit() for character in password):
        raise NumberError("Password must contain at least one number")

    print("Password is valid")
except (PasswordLengthError, UppercaseError, NumberError) as error:
    print("Invalid password:", error)
