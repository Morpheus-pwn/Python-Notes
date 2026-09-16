class Student:
    course = "python" #class attribute
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

s1=Student("pawan", 88) # instance attribute
s2=Student("shaji", 95)
print(s1.name,s1.course)
print(s1.mark)
print(s2.name,s2.course)
print(s2.mark)

class Example:
    public=1
    _protected=2
    def __init__(self):
        self.__private=3

    def show(self):
        self.__privatep=4
        print(self.__privatep)

e=Example()
print(e.public)
print(e._protected)
print(e._Example__private)
e.show()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4*4 #instantiation: object of the class cannot be created because it has abstract methods that have not been implemented. The abstract method area() is implemented in the Square class, so we can create an object of the Square class and call the area() method.

s=Square()
print(s.area())

class Demo:
    def show(self):
        print("instance method") 

d=Demo()
d.show()

#there is no decorator or annotation before the method definition, so it is an instance method. It can be called on an instance of the class.

class Demo:
    @classmethod 
    def show(cls): #cls=class name
        print("class method")

d=Demo()
Demo.show()

class Demo:
    @staticmethod
    def show():
        print("static method")

Demo.show()

class Student:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("name: ", self.name)

s=Student("pawan")
s.show()
d=Student("shaji")
d.show()

# composition and inheritance
# inheritance: _is a relationship
# composition: _has a relationship

# object lifecycle and scope

class Bankbalance:
    def __init__(self, balance=1000):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            raise ValueError("Insufficient balance")

bank = Bankbalance()
print("Initial balance:", bank._balance)
bank.deposit(500)
print("Balance after deposit:", bank._balance)
bank.withdraw(200)
print("Balance after withdrawal:", bank._balance)
# bank.withdraw(2000)