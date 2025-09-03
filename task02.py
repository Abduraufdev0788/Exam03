class Student:
    def __init__(self, name, age, study):
        self.name = name
        self.age = age
        self.study = study
    
    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old, studying in {self.study}nd course."
    
s = Student("Ali", 20, 2)
print(s.introduce())
