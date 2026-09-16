class student:
    __private=3

s=student()
# print(s.__private)
print(s._student__private) #name mangling

class student:
    name="alice"

s=student()
print(s.name)

class account:
    _balance=1000 #protected attribute

class savingsAccount(account):
    def show_balance(self):
        print(self._balance)

acc=savingsAccount()
acc.show_balance()
print(acc._balance) #accessing protected attribute outside class

inheritance avoids code repetition

single level inheritance
class animal:
    def speak(self):
        print("animal makes a sound")

class dog(animal):
    def bark(self):
        print("dog barks")

d=dog()
d.speak()
d.bark()

multi-level inheritance
class animal:
    def speak(self):
        print("animal makes a sound")

class dog(animal):
    def bark(self):
        print("dog barks")

class puppy(dog):
    def cry(self):
        print("puppy cries")

p=puppy()
p.speak()
p.bark()
p.cry()

d=dog()
d.speak()
d.bark()

a=animal()
a.speak()

hierarchical inheritance

class animal:
    def speak(self):
        print("animal makes a sound")

class dog(animal):
    def bark(self):
        print("dog barks")

class cat(animal):
    def meow(self):
        print("cat meows")

c=cat()
c.speak()
c.meow()

d=dog()
d.speak()
d.bark()

a=animal()
a.speak()

multiple inheritance

class father:
    def cooking(self):
        print("father can cook")

class mother:
    def cooking(self):
        print("mother can cook")

class child(father,mother):
    pass

c=child()
c.cooking()

hybrid inheritance (hybrid = hierarchical + multiple)

class animal:
    def speak(self):
        print("animal makes a sound")

class dog(animal):
    def speak(self):
        super().speak()
        print("dog barks")

d=dog()
d.speak()

1
class Vehicle:
    def __init__(self):
        self.brand="Toyota"
        self.price=2000000

class Car(Vehicle):
    def display_car_details(self):
        self.number_of_doors=4
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Number of Doors:",self.number_of_doors)

c=Car()
c.display_car_details()

#2
class vehicle:
    def __init__(self):
        self.brand="Tata"
        print("brand: ", self.brand)

class car(vehicle):
    def model(self):
        self.model="nexon"
        print("model: ", self.model)

class electric_car(car):
    def battery_capacity(self):
        self.battery_capacity="30kWh"
        print("battery capacity: ", self.battery_capacity)

e=electric_car()
e.model()
e.battery_capacity()

#3
class Employee:
    def display_employee(self):
        self.name="pawan"
        self.salary=50000
        print("name: ", self.name)
        print("salary: ", self.salary)

class Developer(Employee):
    def programming_language(self):
        self.language="python"
        print("programming language: ", self.language)

class Designer(Employee):
    def design_tool(self):
        self.tool="photoshop"
        print("design tool: ", self.tool)

d=Developer()
d.programming_language()

e=Designer()
e.design_tool()

#4
class phone:
    def make_call(self):
        print("making a call")

class camera:
    def take_photo(self):
        print("taking a photo")

class smartphone(phone,camera):
    pass

s=smartphone()
s.make_call()
s.take_photo()


polymorphism: same method name but different implementation or behavior in different classes

class Dog:
    def speak(self):
        print("woof!")

class Cat:
    def speak(self):
        print("meow!")

animals=[Dog(), Cat()] #duck typing: python does not check the type of object, it checks for the presence of a method or attribute

for a in animals:
    a.speak()

class File:
    def read(self):
        print("reading file")

class Socket:
    def read(self):
        print("reading socket")

def fetch_data(source):
    source.read()

fetch_data(File())
fetch_data(Socket())

operator overloading: same operator but different implementation or behavior in different classes

class Point:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):
        return self.x+other.x

p1=Point(5)
p2=Point(10)
print(p1+p2)

p1+p2 -> p1 __add__ p2

__add__ is dunder method (double underscore method) or magic method

A shopping cart contains the total price of the items.
Create a Cart class with:

total as an attribute
__add__() to combine the totals of two carts

class Cart:
    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return self.total + other.total

cart1 = Cart(100)
cart2 = Cart(200)
print(cart1 + cart2)

Create a Person class with:

name
age

Use the __ge__() special method to compare a person's age with the minimum voting age of 18.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ge__(self, other):
        if(self.age >= other):
            return "eligible to vote"
        else:
            return "not eligible to vote"

p=Person("Alice", 16)
print(p >= 18)

Encapsulation

class Student:
    def __init__(self):
        self.marks = 0  # public attribute
    @property
    def marks(self):
        return self.__marks  # private attribute

    @marks.setter
    def marks(self, value):
        if value<0:
            print("invalid marks")
        else:
            self.__marks = value

s = Student()
s.marks = 80
print(s.marks)

class student:
    def __init__(self):
        self.__marks=80

s=student()

print(s.marks)
s.marks=80
print(s.marks)

class student:
    def __init__(self):
        self.__marks=80

    def my_marks(self):
        print(self.__marks)

s=student()
s.my_marks()

class student:
    def __init__(self):
        self.__marks=80

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if value<0:
            print("invalid marks")
        else:
            self.__marks = value

s=student()
print(s.get_marks())
s.set_marks(-1)
print(s.get_marks())