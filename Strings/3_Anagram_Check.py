first = input("Enter first string: ")
second = input("Enter second string: ")

first_clean = sorted(first.replace(" ", "").lower())
second_clean = sorted(second.replace(" ", "").lower())

if first_clean == second_clean:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
