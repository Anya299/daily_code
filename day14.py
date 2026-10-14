#1. Inheritance

#Inheritance allows one class to reuse functionality from another class.

Parent class
class Animal:

    def eat(self):
        print("Animal is eating.")
Child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking.")

#Now:

#dog = Dog()

#dog.eat()
#dog.bark()

#Output:

#Animal is eating.
#Dog is barking.

#The Dog class inherited eat() from Animal.

#Interview definition

#Inheritance allows a child class to reuse and extend the attributes and methods of a parent class.

#2. Constructor inheritance

#Consider:

class Animal:

    def __init__(self, name):
        self.name = name

#Child:

class Dog(Animal):
    pass

#Then:

dog = Dog("Bruno")

print(dog.name)

#works because Dog inherits the parent's constructor.

#3. Method overriding

#A child class can provide its own implementation of a method.

class Animal:

    def sound(self):
        print("Some animal sound.")


class Dog(Animal):

    def sound(self):
        print("Bark")

#Now:
animal = Animal()
dog = Dog()

animal.sound()
dog.sound()

#Output:

Some animal sound.
Bark

#The child's sound() overrides the parent's sound().

#4. super()

#Sometimes the child needs the parent's implementation.

class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

#Now:

dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)

#Output:

#Bruno
#Labrador
#What happened?
#super().__init__(name)

#calls the parent class's constructor.

#Think:

#super() → parent class
#Interview answer

#super() is used to access methods or constructors of the parent class from a child class.

35. Polymorphism

#Poly = many
3Morph = forms

#Different objects can respond to the same method name in different ways.

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

#Output:

#Bark
#Meow

#Same:

#animal.sound()

#Different behavior depending on the object.

#That's polymorphism.

#6. Python's duck typing

#Python often doesn't care about the object's exact class.

#It cares whether the object provides the required behavior.

class Dog:

    def speak(self):
        print("Bark")


class Person:

    def speak(self):
        print("Hello")


def make_speak(obj):
    obj.speak()

#Now:

make_speak(Dog())
make_speak(Person())

#Both work.

#Because both objects have:

#speak()

#This idea is commonly called duck typing.

#"If it behaves like the required object, Python can use it."

#7. Abstract classes

#Sometimes we want to define a common structure that child classes must implement.

#Python provides ABC.

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

#Now:

class Dog(Animal):

    def sound(self):
        print("Bark")

#But this:

#animal = Animal()

#will fail because Animal has an abstract method.

#The child must implement:

#sound()
#Why use abstract classes?

#They define a contract.

#For example:
'''
Payment
   ↓
 ┌───────────────┐
 │               │
UPI           CreditCard

Every payment type might be required to implement:

pay()'''
#8. Composition

#This is extremely important for real software engineering.

#Composition means:

#One class contains an object of another class.

#Example:

class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started.")
'''
Here:

Car
 ↓
contains
 ↓
Engine

This is composition.'''

#9. Inheritance vs composition

#Remember this simple distinction:

#Inheritance
#Dog IS an Animal
class Dog(Animal):
#Composition
#Car HAS an Engine
class Car:
    def __init__(self):
        self.engine = Engine()

#Interview question:

#When should you use inheritance?

#When there is a genuine is-a relationship and the child naturally extends the parent.

#Composition is often used for has-a relationships.


# Day 14 - OOP III
# Inheritance, Overriding, super(), Polymorphism, Composition


# --------------------------------------------------
# 1. Inheritance
# --------------------------------------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking.")


dog = Dog("Bruno")

dog.eat()
dog.bark()


# --------------------------------------------------
# 2. Method Overriding
# --------------------------------------------------

class Animal:

    def sound(self):
        print("Some animal sound.")


class Cat(Animal):

    def sound(self):
        print("Meow")


animal = Animal()
cat = Cat()

animal.sound()
cat.sound()


# --------------------------------------------------
# 3. super()
# --------------------------------------------------

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")


student = Student("Ananya", "AI & Data Science")

student.display()


# --------------------------------------------------
# 4. Polymorphism
# --------------------------------------------------

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# --------------------------------------------------
# 5. Abstract Class
# --------------------------------------------------

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1000)


# --------------------------------------------------
# 6. Composition
# --------------------------------------------------

class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started.")


car = Car()

car.start()
