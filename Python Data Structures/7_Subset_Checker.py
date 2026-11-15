set_a = set(map(int, input("Enter elements of first set: ").split()))
set_b = set(map(int, input("Enter elements of second set: ").split()))

if set_a.issubset(set_b):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")
