class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        new_real = self.r + c2.r
        new_imaginary = self.i + c2.i
        return Complex(new_real, new_imaginary)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

# Option 1: Print each object individually
print(c1)
print(c2)

# Option 2: Print them together using string formatting
print(f"c1: {c1}, c2: {c2}")
