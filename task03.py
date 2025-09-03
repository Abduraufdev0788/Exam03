class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("woof woof")

d = Dog("Rex")
print(d.name)
d.bark()
