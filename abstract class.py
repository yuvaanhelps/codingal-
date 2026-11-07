# import necessary modules
from abc import ABC, abstractmethod

# create base class
class absclass(ABC):
    # function to print a value
     def print(self, x):
             print("passed:",x)
    # abstract method
     @abstractmethod
     def task(self):
             print("we are inside absmethord class")
# create sub class
class test_class(absclass):
      def task(self):
            print("we are inside test_class")
# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)



        
