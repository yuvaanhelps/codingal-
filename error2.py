try:
    num1 , num2= eval(input("enter two numbers , seperated by a comma :"))
    result= num1/num2
    print("result is", result)
# using multiple except block for different types of error 
except ZeroDivisionError:
    print("division by zero is error !!!")
except SyntaxError:
    print("comma is missing . enter numbers seperated by commas like this 1,2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")