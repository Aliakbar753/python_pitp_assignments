import Animal

class Cat(Animal.Animal):

    def walk(self):
        print(f"{self.Name} is walking")

cat = Cat("ketti")
cat.sound()
cat.eat()
cat.walk()