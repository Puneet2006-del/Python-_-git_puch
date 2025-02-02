class Vector:
    def __init__(self, *components):
        self.components = components
        self.dimension = len(components)

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Vectors must be of the same dimension to add.")
        # Calculate the sum of corresponding components
        new_components = tuple(x + y for x, y in zip(self.components, other.components))
        return Vector(*new_components)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.dimension != other.dimension:
                raise ValueError("Vectors must be of the same dimension to calculate dot product.")
            # Calculate the dot product
            dot_product = sum(x * y for x, y in zip(self.components, other.components))
            return dot_product
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            new_components = tuple(other * x for x in self.components)
            return Vector(*new_components)
        else:
            raise TypeError("Multiplication is not defined for the given operands.")

    def __str__(self):
        return f"Vector{self.components}"

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Addition of vectors
v3 = v1 + v2
print(f"v1 + v2 = {v3}")

# Dot product of vectors
dot_product = v1 * v2
print(f"v1 * v2 (dot product) = {dot_product}")

# Scalar multiplication
v4 = v1 * 2
print(f"v1 * 2 = {v4}")
