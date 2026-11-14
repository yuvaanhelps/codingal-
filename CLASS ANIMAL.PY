# import necessary packages
from abc import ABC, abstractmethod
# create a base class
class Animal(ABC):
    # abstract method 
    # should be implimented by all sub classes
    @abstractmethod
    def move(self):
        pass
# subclasses
class human(Animal):
    def move (self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("i can crawl")
class dog(Animal):
    def move (self):
        print("i can bark and run")
class lion(Animal):
    def move(self):
        print("i can run and roar")

# driver code
R = human()
R.move()

k = snake()
k.move()

R = dog()
R.move()

K = lion()
K.move()