import random

# Number 1


class Animal():
    def __init__(self, name: str, age: int, food: list):
        self.__name = name
        self.__age = age
        self.__food = food

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
        return self.__age

    def get_food(self):
        return self.__food

    def add_food(self, new_food):
        self.__food.append(new_food)

        return self.__food

    def remove_food(self, fd):
        for i in self.__food:
            if i == fd:
                self.__food.remove(fd)

        return self.__food

    def talk(self):
        return 0


class Cat(Animal):
    def __init__(self, name: str, age: int, food: list):
        super().__init__(name, age, food)

    def talk(self):
        return "meow"


class Dog(Animal):
    def __init__(self, name: str, age: int, food: list):
        super().__init__(name, age, food)

    def talk(self):
        return "woof woof"


class Fish(Animal):
    def __init__(self, name: str, age: int, food: list):
        super().__init__(name, age, food)

    def talk(self):
        return "blub"


class Cow(Animal):
    def __init__(self, name: str, age: int, food: list):
        super().__init__(name, age, food)

    def talk(self):
        return "muuuuu"

# Number 2


def snail_climb(depth):
    return(str(depth//5) + " days.")

# Number 3


def largest_number(arr):
    return max(arr)

# Number 4


def calc_case(word):
    upper = 0
    lower = 0
    for i in word:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    return "UPPER CASE " + str(upper) + " LOWER CASE " + str(lower)

# Number 5


class Dice_Game():
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
        self.score_a = 0
        self.score_b = 0

    def play(self):
        if self.score_a or self.score_b != 5:
            print("Player A Makes Move")
            print("Player A scored ", self.roll())
            score_a += self.roll()

            print("Player B Makes Move")
            print("Player B scores ", self.roll())
            score_b += self.roll()

    def roll(self):
        return random.randrange(1, 5)

# Number 6


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Animal("kujo", 2)
print(dir(dog))

# Number 7


class Stack:
    def __init__(self):
        self.stack = list()

    # check if the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        # push element on the stack
        self.stack.append(data)

    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

# Number 8


print([i**2 for i in range(1, 3)])


if __name__ == "__main__":
    pass
