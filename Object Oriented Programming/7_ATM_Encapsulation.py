class ATM:
    def __init__(self, pin, balance):
        self.__pin = str(pin)
        self.__balance = balance

    def verify_pin(self, entered_pin):
        return self.__pin == str(entered_pin)

    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print("Available balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self, entered_pin, amount):
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN")
        elif amount <= 0:
            print("Enter a valid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.__balance)

atm = ATM("1234", 10000)
pin = input("Enter PIN: ")
atm.check_balance(pin)

amount = float(input("Enter withdrawal amount: "))
atm.withdraw(pin, amount)
