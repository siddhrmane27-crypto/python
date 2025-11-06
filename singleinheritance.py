# Single Inheritance Example
class Parent:
    def feature1(self):
        print("Feature 1 from Parent")

class Child(Parent):
    def feature2(self):
        print("Feature 2 from Child")

c = Child()
c.feature1()
c.feature2()
