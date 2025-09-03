class Vector:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __add__(self, other):
        return Vector(self.v1 + other.v1, self.v2 + other.v2)

    def __repr__(self):
        return f"Vector({self.v1}, {self.v2})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)
