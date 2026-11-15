text = input("Enter a string: ")

cleaned_text = "".join(text.lower().split())

if cleaned_text == cleaned_text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
