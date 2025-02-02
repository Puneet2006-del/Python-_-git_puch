class Vector:
    def __init__(self, *components):
        if len(components) != 3:
            raise ValueError("Vector must have exactly 3 components (i, j, k)")
        self.components = components

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and {}".format(type(other).__name__))
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(other * a for a in self.components))
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and {}".format(type(other).__name__))

    def __str__(self):
        return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"

# Example usage:
v1 = Vector(7, 8, 10)
print(v1)  # Output: 7i + 8j + 10k

v2 = Vector(1, 2, 3)
print(v2)  # Output: 1i + 2j + 3k

# Addition of vectors
v3 = v1 + v2
print(v3)  # Output: 8i + 10j + 13k

# Dot product of vectors
dot_product = v1 * v2
print(dot_product)  # Output: 53

# Scalar multiplication
v4 = v1 * 2
print(v4)  # Output: 14i + 16j + 20k
