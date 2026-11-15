balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

try:
    if withdrawal > balance:
        raise ValueError("Withdrawal exceeds available balance")
    if withdrawal <= 0:
        raise ValueError("Withdrawal amount must be positive")
    balance -= withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)
except ValueError as error:
    print("Exception:", error)
