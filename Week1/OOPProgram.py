from abc import ABC, abstractmethod   # ABC -> base class for abstract classes


# Abstract Base Class (ABC)
class Person(ABC):
    def __init__(self, name, age):
        self.name = name          # Public
        self._age = age           # Protected
        self.__country = "India"  # Private

    @abstractmethod
    def get_role(self):
        pass

    def get_country(self):
        return self.__country


# Inheritance + Method Overriding
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)   # Calls parent constructor
        self.marks = marks

    def get_role(self):
        return "Student"

    # Magic method: __len__
    def __len__(self):
        return len(self.name)


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_role(self):
        return "Teacher"


# Method Overloading 
class Calculator:
    def add(self, a, b=0):
        return a + b

# Object Creation
s1 = Student("Sita Soni", 20, 80)
s2 = Student("Aman Jain", 22, 90)
t1 = Teacher("Ambika Mishra", 40, 50000)

print(s1.name, "is a", s1.get_role())
print(t1.name, "is a", t1.get_role())

# Encapsulation
print("Country:", s1.get_country())

print("Length of name:", len(s1))   

# Method overloading
calc = Calculator()
print("Add:", calc.add(5))
print("Add:", calc.add(5, 10))
