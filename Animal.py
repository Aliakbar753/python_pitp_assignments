class Animal:
    Name = ""

    def __init__(self,name):
        self.Name = name

    def sound(self):
        print(f"{self.Name} sounds")

    def eat(self):
        print(f"{self.Name} is eating")
