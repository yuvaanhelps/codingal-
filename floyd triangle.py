# take input from user
rows= int(input("please enter the number of  rows"))
number= 1 # initilise by 1
print("floyds's triangle")
# outer loop for the number of rows
for i in range(1, rows+1):
    # iner loop for number of columns
    for j in range(1, i+1):
        # display result
        print(number, end ='')
        number = number+1
    print()


