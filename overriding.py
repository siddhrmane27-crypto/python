#method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
# Create instances

A=Animal()
D=Dog()
C=Cat()
D.sound()
C.sound()