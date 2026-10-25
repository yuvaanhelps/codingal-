# create class
class IOString():
    # constructor to set default value
    def __init__(self, string):
        self.str1= ""
        # function to get input from user
    def get_string(self):
        self.str1 = input("Enter a string: ")
        # function to print string in upper case
    def print_string(self):
        print(self.str1.upper())
# object creation
str1= IOString("")
# call functions
str1.get_string()
str1.print_string()