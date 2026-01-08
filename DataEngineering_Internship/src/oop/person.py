from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__country = "India"

    @abstractmethod
    def get_role(self):
        pass

    def get_country(self):
        return self.__country


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def get_role(self):
        return "Student"

    def __len__(self):
        return len(self.name)


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_role(self):
        return "Teacher"


class Calculator:
    def add(self, a, b=0):
        return a + b


if __name__ == "__main__":
    s1 = Student("Sita Soni", 20, 80)
    t1 = Teacher("Ambika Mishra", 40, 50000)

    print(s1.name, s1.get_role())
    print(t1.name, t1.get_role())
    print("Country:", s1.get_country())
    print("Name length:", len(s1))
