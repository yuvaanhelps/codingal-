# Input a number
num = int(input("Enter a number: "))

# Convert to positive in case of negative numbers
num = abs(num)

# Count digits
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1

print("Number of digits:", count)