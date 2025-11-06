from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")


class bike(Vehicle):
    def start(self):
        print("Bike started.")


class aeroplane(Vehicle):
    def start(self):
        print("Aeroplane is flying.")


c=Car()
c.start()

b=bike()
b.start()

a=aeroplane()
a.start()

