class Animal:
    name = ""
    sound = ""
    eat = ""


    def __init__(self, name, sound, eat):
        self.name = name
        self.sound = sound
        self.eat = eat

    def speak(self):
        print(f"{self.name} says {self.sound} and {self.name} eats {self.eat}" )

dog = Animal("Dog", "waof","meat")
cat = Animal('cat', 'meow',"milk")
dog.speak()
cat.speak( )

 