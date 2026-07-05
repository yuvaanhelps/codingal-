# Read the number of rows from the user
n = int(input("Enter the number of rows: "))

# Outer loop controls the number of rows
for i in range(1, n + 1):

    # Print spaces before the stars
    # Number of spaces decreases with each row
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    # Number of stars increases with each row
    for j in range(i):
        print("*", end="")

    # Move to the next line after each row
    print()