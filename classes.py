from calendar import c
from datetime import datetime


# Number 1

class CreditCard():
    def __init__(self, card_number: str, security_code: int, exp_date):
        self.card_number = card_number
        self.security_code = security_code
        self.exp_date = datetime.strptime(exp_date, '%b %d %Y')

    def get_details(self):
        return self.card_number + " " + str(self.exp_date) + " " + str(self.security_code)


my_cred_card = CreditCard("4xf5-tyv4-54#w", 4567, "Dec 1 1995")
print(my_cred_card.get_details())


# Number 2
class Animal():
    def __init__(self):
        pass


class Dog(Animal):
    def bark(self):
        print("woof woof")


dog = Dog()
dog.bark()


# Number 3
class Queue():
    arr = []

    def enqueue(self, element):
        self.arr.append(element)

    def dequeue(self):
        self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def display(self):
        return self.arr


c = Queue()
c.enqueue("police")
c.enqueue("mambo")
c.enqueue("jambo")
print(c.size())
print(c.display())

c.dequeue()

print(c.display())

# Number 4


class Stack():
    arr = []

    def push(self):
        pass

    def pop(self):
        pass

    def size(self):
        pass


# Number 5
class Person():

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def work(self):
        print(self.name + " is working.")


# Number 6

class Employee():
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def work(self):
        print(self.name + " is working.")


class Programmer(Employee):
    def __init__(self, langauge, name, age, salary):
        super().__init__(name, age, salary)

        self.langauge = langauge

    def code(self):
        print(self.name, " is coding.")


j = Programmer("Python", "John", 15, 200000)
j.code()

# Number 7.


class Vehicle():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.make, " ", self.model, " ", self.year, " is starting.")

    def stop(self):
        print(self.make, " ", self.model, " ", self.year, " is stopping.")

    def drive(self):
        print(self.make, " ", self.model, " ", self.year, " is driving.")


class Car(Vehicle):
    def __init__(self, make, model, year, colour):
        super().__init__(make, model, year)

        self.colour = colour

    def park(self):
        print(self.make, " ", self.model, " ",
              self.year, " ", self.colour, " is parkng.")


m = Car("Mercedes", "c-class", 2020, "black")
m.start()
m.drive()
m.stop()
m.park()

# Number 8


class Animal():
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def make_sound(self):
        print(self.name + " is making a sound.")


class Dog(Animal):
    def __init__(self, name, colour, age, breed):
        super().__init__(name, colour, age)

        self.breed = breed

    def bark(self):
        print(self.name, "is barking.")


k = Dog("Kujo", "black and white spots", 2, "german shepherd")
k.eat()
k.sleep()
k.bark()
k.make_sound()


# Number 9.

class Locomotive():
    def __init__(self, type, number_of_tyres: int):
        self.type = type
        self.number_of_tyres = number_of_tyres

    @staticmethod
    def locomotive_type():
        print("this is a static method.")

    def get_number_of_tyres(self):
        return str(self.number_of_tyres) + "tyres."

    def locomotive_details(self):
        return 0


class Evehicle(Locomotive):

    def __init__(self, name, year, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = name
        self.__year = year

    def __repr__(self) -> str:
        return self.name

    def get_year(self):
        print(self.__year)

    def locomotive_details(self):
        return "Type: " + self.type + " No. Tyres: " + str(self.number_of_tyres)
