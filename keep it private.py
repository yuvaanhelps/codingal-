# class creation 
class myclass:
    # private variable
    __privateVar = 45;
    # private method
    def __privMeth(self):
        print("i am in a class in myclass")
    # function to print value of private variable
    def hello(self):
        print("private value number is:", myclass.__privateVar)

 # object creation and methord call
obj = myclass()
obj.hello()
obj.__privMeth()  