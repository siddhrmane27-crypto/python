# method overloading in python

class Maths:
    # Method with default arguments
    def add(self, a=0, b=0, c=0):
        print("Sum:", a + b + c)

m = Maths()

m.add(5, 10)      # Adds 2 numbers
m.add(5, 10, 15)  # Adds 3 numbers
m.add(5)          # Adds 1 number




print("\n")
print("with *args")

# Using *args to handle variable number of arguments
class MathOperations:
    def add(self, *args):
        total = sum(args)
        print("Sum:", total)

m = MathOperations()

m.add(5, 10)           # Adds 2 numbers
m.add(1, 2, 3)         # Adds 3 numbers
m.add(4, 5, 6, 7, 8)   # Adds 5 numbers
