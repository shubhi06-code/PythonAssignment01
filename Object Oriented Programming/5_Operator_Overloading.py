class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def display(self):
        sign = "+" if self.imaginary >= 0 else "-"
        print(f"{self.real} {sign} {abs(self.imaginary)}i")

first = Complex(3, 4)
second = Complex(2, 5)
result = first + second

print("First complex number:")
first.display()
print("Second complex number:")
second.display()
print("Sum:")
result.display()
