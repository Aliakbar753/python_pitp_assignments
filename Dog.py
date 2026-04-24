import Animal
class Dog(Animal.Animal):

    def fetch(self):
        print(f"{self.Name} is fetching")


dog = Dog("Buddy")
dog.sound()
dog.eat()
dog.fetch()