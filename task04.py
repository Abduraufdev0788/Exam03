class Flyer:
    def fly(self):
        print("Duck is flying")

class Swimer:
    def swim(self):
        print("Duck is swimming")

class Duck(Flyer, Swimer):
    pass

duck = Duck()
duck.fly()
duck.swim()
        