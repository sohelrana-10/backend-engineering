
# ==========================================
# 1. SINGLE INHERITANCE
# One child class inherits from one parent
# ==========================================

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


class Employee(Person):
    def work(self):
        print(f"{self.name} is working.")


print("\n--- Single Inheritance ---")

employee = Employee("Sohel")
employee.introduce()  # Inherited method
employee.work()       # Own method


# ==========================================
# 2. MULTIPLE INHERITANCE
# One child inherits from multiple parents
# ==========================================

class Programmer:
    def write_code(self):
        print("Writing Python code.")


class Designer:
    def design_ui(self):
        print("Designing the user interface.")


class Developer(Programmer, Designer):
    def develop(self):
        print("Developing an application.")


print("\n--- Multiple Inheritance ---")

developer = Developer()
developer.write_code()  # From Programmer
developer.design_ui()   # From Designer
developer.develop()     # Own method


# ==========================================
# 3. MULTILEVEL INHERITANCE
# A class inherits from a child class
# in a chain of inheritance
# ==========================================

class Animal:
    def eat(self):
        print("Animal is eating.")


class Mammal(Animal):
    def breathe(self):
        print("Mammal is breathing.")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking.")


print("\n--- Multilevel Inheritance ---")

dog = Dog()
dog.eat()      # From Animal
dog.breathe()  # From Mammal
dog.bark()     # Own method


# ==========================================
# 4. HIERARCHICAL INHERITANCE
# Multiple child classes inherit from one parent
# ==========================================

class Vehicle:
    def start(self):
        print("Vehicle started.")


class Car(Vehicle):
    def drive(self):
        print("Car is driving.")


class Bike(Vehicle):
    def ride(self):
        print("Bike is being ridden.")


print("\n--- Hierarchical Inheritance ---")

car = Car()
car.start()  # From Vehicle
car.drive()  # Own method

bike = Bike()
bike.start()  # From Vehicle
bike.ride()   # Own method


# ==========================================
# 5. HYBRID INHERITANCE
# A combination of two or more inheritance types
# ==========================================

class PersonBase:
    def identify(self):
        print("I am a person.")


class EmployeeBase(PersonBase):
    def work(self):
        print("I work for a company.")


class StudentBase(PersonBase):
    def study(self):
        print("I am studying.")


class Intern(EmployeeBase, StudentBase):
    def train(self):
        print("I am an intern.")


print("\n--- Hybrid Inheritance ---")

intern = Intern()
intern.identify()  # From PersonBase
intern.work()      # From EmployeeBase
intern.study()     # From StudentBase
intern.train()     # Own method

# Check Method Resolution Order (MRO)
print("\nMRO:", [cls.__name__ for cls in Intern.mro()])
