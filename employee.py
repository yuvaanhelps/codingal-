# create class
class employee:
    # initilizing
    def __init__(self):
        print("employee created")
    # call distructor
    def __del__(self):
        print(" distructor called.")
def create_obj():
    print("making object")
    emp = employee()
    print("function ended")
    return object
print("calling create_obj() function")
obj = create_obj()
print("program ended")

