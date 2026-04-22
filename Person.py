class Person:
    name= ""
    age=0

    def intro(self,name,age):
        self.name = name
        self.age = age

        print(f"My name is {self.name}, MY ag is {self.age}")

person1 = Person()

person1.intro('ali', 23) 