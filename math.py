# Input three values
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

# Swapping
temp = a
a = b
b = c
c = temp

# Output
print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)