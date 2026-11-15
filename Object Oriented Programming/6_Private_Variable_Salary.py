class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

employee = Employee(30000)
print("Salary:", employee.get_salary())

new_salary = float(input("Enter new salary: "))
employee.set_salary(new_salary)

print("Updated Salary:", employee.get_salary())
